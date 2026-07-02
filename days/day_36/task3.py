class APIRouter:
    def setup(self):
        self.routes = []

    def add_route(self, path):
        self.routes.append(path)

    def show_routes(self):
        print(f"Active routes: {', '.join(self.routes)}")
router = APIRouter()
router.setup()
router.add_route("/users")
router.add_route("/post")
router.show_routes()