# class Element:
#     def __add__(self, other):
#         return None


# class Water(Element):
#     def __add__(self, other):
#         if isinstance(other, Air):
#             return Storm()
#         elif isinstance(other, Fire):
#             return Steam()
#         elif isinstance(other, Earth):
#             return Mud()
#         else:
#             return super().__add__(other)


# class Air(Element):
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Lightning()
#         elif isinstance(other, Earth):
#             return Dust()
#         elif isinstance(other, Water):  # For symmetry
#             return Storm()
#         else:
#             return super().__add__(other)


# class Fire(Element):
#     def __add__(self, other):
#         if isinstance(other, Earth):
#             return Lava()
#         elif isinstance(other, Water):
#             return Steam()
#         elif isinstance(other, Air):  # For symmetry
#             return Lightning()
#         else:
#             return super().__add__(other)


# class Earth(Element):
#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Mud()
#         elif isinstance(other, Air):
#             return Dust()
#         elif isinstance(other, Fire):
#             return Lava()
#         else:
#             return super().__add__(other)


# # Defining new elements
# class Storm(Element):
#     pass

# class Steam(Element):
#     pass

# class Mud(Element):
#     pass

# class Lightning(Element):
#     pass

# class Dust(Element):
#     pass

# class Lava(Element):
#     pass

# # Custom element
# class Ice(Element):
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Water()
#         elif isinstance(other, Earth):
#             return "FrostRock"  # New custom element
#         else:
#             return super().__add__(other)

# # Testing the elements
# water = Water()
# air = Air()
# fire = Fire()
# earth = Earth()
# ice = Ice()

# # Test combinations
# print(type(water + air))  # Should be Storm
# print(type(fire + earth))  # Should be Lava
# print(type(ice + fire))    # Should be Water
# print(type(ice + earth))   # Should be 'FrostRock' (custom element)
