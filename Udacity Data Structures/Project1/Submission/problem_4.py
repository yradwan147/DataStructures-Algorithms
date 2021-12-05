class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
parent.add_user('sub_child_usr')
child.add_user('tester1')


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    return check_group(user, group) > 0


def check_group(user, group):
    if user in group.users:
        res = 1
    else:
        res = 0
    for subgroup in group.groups:
        res += check_group(user, subgroup)
    return res


# True
print(is_user_in_group('sub_child_usr', parent))
print(is_user_in_group('sub_child_user', parent))
print(is_user_in_group('tester1', child))

# False
print(is_user_in_group('tester2', parent))
print(is_user_in_group('', parent))
