class ApiResponse:
    def __init__(self, status_code: int, body: str):
        self.status_code = status_code
        self.body = body