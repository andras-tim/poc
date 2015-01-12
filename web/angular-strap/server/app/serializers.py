from marshmallow import Serializer, fields


class UserSerializer(Serializer):
    class Meta:
        fields = ("id", "email")


class TaskSerializer(Serializer):
    user = fields.Nested(UserSerializer)
 
    class Meta:
        fields = ("id", "title", "description", "done", "user", "created_at")
