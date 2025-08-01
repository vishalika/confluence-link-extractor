import streamlit as st
import requests
import pandas as pd
import io

st.set_page_config(page_title="Confluence Page Link Extractor", layout="centered")
st.title("🔗 Confluence Page Link Extractor")

# User inputs

base_url = st.text_input(
    "Confluence Base URL",
    placeholder="e.g., https://yourcompany.atlassian.net/wiki",
    help="Enter the base URL of your Confluence instance. It usually ends with /wiki."
)

space_key = st.text_input(
    "Confluence Space Key",
    placeholder="e.g., ENG, HR, TSSG",
    help="Enter the key of the Confluence space you want to extract page links from."
)

email = st.text_input(
    "Atlassian Email",
    placeholder="your.email@company.com",
    help="Enter the email associated with your Atlassian account."
)

api_token = st.text_input(
    "API Token",
    type="password",
    help="Generate your API token from https://id.atlassian.com/manage-profile/security/api-tokens"
)

if st.button("Fetch Page Links"):
    if not all([base_url, space_key, email, api_token]):
        st.warning("Please fill in all fields.")
    else:
        with st.spinner("Fetching pages..."):
            auth = (email, api_token)
            headers = {"Accept": "application/json"}
            page_links = []
            start = 0
            limit = 50

            while True:
                url = f"{base_url}/rest/api/content?spaceKey={space_key}&type=page&limit={limit}&start={start}&expand=ancestors"
                response = requests.get(url, auth=auth, headers=headers)
                if response.status_code != 200:
                    st.error(f"Failed to fetch pages: {response.status_code}")
                    break

                data = response.json()
                results = data.get("results", [])
                if not results:
                    break

                for page in results:
                    title = page["title"]
                    page_id = page["id"]
                    ancestors = page.get("ancestors", [])

                    # Exclude archived pages
                    if any("archive" in ancestor.get("title", "").lower() for ancestor in ancestors):
                        continue

                    page_url = f"{base_url}/spaces/{space_key}/pages/{page_id}/{title.replace(' ', '+')}"
                    page_links.append({"Title": title, "URL": page_url})

                if "_links" in data and "next" in data["_links"]:
                    start += limit
                else:
                    break

            if page_links:
                df = pd.DataFrame(page_links)
                st.success(f"✅ Found {len(df)} pages.")
                st.dataframe(df)

                # Convert DataFrame to Excel in memory
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False)
                output.seek(0)

                st.download_button(
                    label="📥 Download Excel",
                    data=output,
                    file_name="confluence_page_links.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            else:
                st.info("No pages found.")
