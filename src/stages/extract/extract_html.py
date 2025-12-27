class ExtractHtml:

    def __init__(self, http_requester, html_colletor) -> None:
        self.__http_requester = http_requester

        self.__html_collector = html_colletor