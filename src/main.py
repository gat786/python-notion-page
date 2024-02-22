import os
from utils import exports

from notion_client import Client

notion = Client(auth=exports.notion_api_token)


def main():
    print("Creating a page")
    page = notion.pages.create(
        parent={"page_id": "b8fc73f0bafc4884ac01da36444967ec"},
        properties={
            "Title": {
                "id": "title",
                "type": "title",
                "title": [
                    {
                        "type": "text",
                        "text": {
                            "content": "A better title for the page"
                        },
                        "annotations": {
                            "bold": False,
                            "italic": False,
                            "strikethrough": False,
                            "underline": False,
                            "code": False,
                            "color": "default",
                        },
                        "plain_text": "This is also not done",
                    }
                ],
            }
        },
        children=[],
        icon={
            "emoji": "😻",
        },
        cover={
            "external": {
                "url": "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7b8b0713-dbd4-4962-b38b-955b6c49a573/My_test_image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221024%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221024T205211Z&X-Amz-Expires=3600&X-Amz-Signature=208aa971577ff05e75e68354e8a9488697288ff3fb3879c2d599433a7625bf90&X-Amz-SignedHeaders=host&x-id=GetObject",
            }
        },
    )
    print(f"page created {page}")


if __name__ == "__main__":
    main()
