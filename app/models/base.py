from sqlalchemy.orm import DeclarativeBase


def to_camel(snake_str: str) -> str:
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

class Base(DeclarativeBase):
    def serialize(self):
        data = {}
        for column in self.__mapper__.columns:
            attr_name = column.key
            camel_key = to_camel(attr_name)
            data[camel_key] = getattr(self, attr_name)
        return data
