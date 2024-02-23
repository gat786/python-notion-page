import os
from utils import exports

from notion_client import Client

notion = Client(auth=exports.notion_api_token)


def main():
    print("Creating a page")
    for i in range(10,13):
        page = notion.pages.create(
            parent={"page_id": "b8fc73f0bafc4884ac01da36444967ec"},
            properties={
                "title": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "mention",
                            "mention": {
                                "type": "date",
                                "date": {
                                    "start": f"2024-02-{i}"
                                }
                            }
                        }
                    ],
                }
            },
            children=[],
            icon={
                "emoji": "😻",
            },
        )
        print(f"page created {page}")


if __name__ == "__main__":
    main()
