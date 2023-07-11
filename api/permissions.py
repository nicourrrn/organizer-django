from rest_framework.permissions import BasePermission 

class IsTaskOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        root = obj 
        while root.parent is not None:
            root = root.parent
        print(obj)
        return request.user.main_task == root
        

