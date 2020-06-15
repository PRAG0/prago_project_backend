from rest_framework import permissions


class UpdateOwnAccount(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # 안전한 메소드, get, head, options로 접근시 true반환 --> api 호출
            return True
        # 그 외의 조작이 가능한 ((문맥상) 안전하지않은)메소드로 요청시, 요청자가 검증된 사용자인지 검사
        # id가 맞으면 True, 아니면 False
        return obj.id == request.user.id