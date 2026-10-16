permissions = {'admin': {'read', 'write', 'delete'}, 'operator': {'read', 'write'}, 'auditor': {'read', 'export'}}
common = set.intersection(*permissions.values())
all_permissions = set.union(*permissions.values())
print("Common permissions:", sorted(common))
print("All permissions:", sorted(all_permissions))