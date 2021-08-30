from http import HTTPStatus

from pyrdf4j.api_base import APIBase
from pyrdf4j.errors import TerminatingError


class APIGraph(APIBase):

    def repo_id_to_uri(self, repo_id, repo_uri=None):
        """Translates a repository ID into a api endpoint URI"""
        if repo_uri is not None:
            return repo_uri
        repo_uri = self.server.RDF4J_base + 'repositories/{}/statements'.format(repo_id)
        return repo_uri

    def replace_triple_data_in_repo(self, repo_id, triple_data, content_type, auth=None, repo_uri=None):
        repo_uri = self.repo_id_to_uri(repo_id, repo_uri=repo_uri)

        headers = {'Content-Type': content_type}
        response = self.server.put(
            repo_uri,
            data=triple_data,
            headers=headers,
            auth=auth,
        )
        if response.status_code != HTTPStatus.NO_CONTENT:
            raise TerminatingError

        return response

    def add_triple_data_to_repo(self, repo_id, triple_data, content_type, auth=None, repo_uri=None):
        repo_uri = self.repo_id_to_uri(repo_id, repo_uri=repo_uri)

        headers = {'Content-Type': content_type}
        response = self.server.post(
            repo_uri,
            data=triple_data,
            headers=headers,
            auth=auth,
        )
        if response.status_code != HTTPStatus.NO_CONTENT:
            raise TerminatingError

        return response