from src.domain.parts import action, part, repository


class PartService:
    """
    Handle the interaction with the parts domain.
    """

    def __init__(self, repository: repository.PartRepository):
        self.repo = repository

    def get_parts(self) -> list[part.Part]:
        """
        Retrieve all parts.
        """
        return self.repo.get_all()

    def create_part(self, cp: action.CreatePart) -> part.Part:
        """
        Create a new part.
        """
        return self.repo.create(cp)

    def delete_part(self, id: int) -> None:
        """
        Delete a part.
        """
        self.repo.delete_by_id(id)

    def create_test(self, cp: action.CreateTest) -> part.Test:
        """
        Create a test for a part.
        """
        return self.repo.create_test(cp)
