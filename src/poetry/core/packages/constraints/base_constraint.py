class BaseConstraint:
    def allows(self, other: "BaseConstraint") -> bool:
        raise NotImplementedError()

    def allows_all(self, other: "BaseConstraint") -> bool:
        raise NotImplementedError()

    def allows_any(self, other: "BaseConstraint") -> bool:
        raise NotImplementedError()

    def difference(self, other: "BaseConstraint") -> "BaseConstraint":
        raise NotImplementedError()

    def intersect(self, other: "BaseConstraint") -> "BaseConstraint":
        raise NotImplementedError()

    def union(self, other: "BaseConstraint") -> "BaseConstraint":
        raise NotImplementedError()

    def is_any(self) -> bool:
        return False

    def is_empty(self) -> bool:
        return False

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {str(self)}>"

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError()
