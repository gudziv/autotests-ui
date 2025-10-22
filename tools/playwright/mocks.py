from playwright.sync_api import  Page


# def abort(route: Route):
#     print(f"\nAborting url: {route.request.url}")
#     route.abort()

def mock_static_resources(page: Page):
    page.route("**/*.{ico,png,jpg,svg,webp,mp3,woff,woff2}", lambda route: route.abort())