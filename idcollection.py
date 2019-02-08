from parse_id import parse_id

class IDCollection:
	def __init__(self):
		self.ids = []
		self.ids_to_objects = {}

	def __len__(self):
		return self.ids_to_objects.__len__()

	def __iter__(self):
		return self.ids_to_objects.__iter__()

	def __contains__(self, needle):
		if hasattr(needle, 'id'):
			return needle.id in self.ids_to_objects
		try:
			id, id_bytes = parse_id(needle)
		except TypeError:
			return False
		except ValueError:
			return False
		else:
			return id in self.ids_to_objects

	def add(self, object):
		if not hasattr(object, 'id'):
			raise ValueError
		self.ids.append(object.id)
		self.ids_to_objects[object.id] = object

	def remove(self, needle):
		if hasattr(needle, 'id') and needle.id in self.ids_to_objects:
			del self.ids_to_objects[needle.id]
			self.ids.remove(needle.id)
			return
		try:
			id, id_bytes = parse_id(needle)
		except TypeError:
			return
		except ValueError:
			return
		else:
			if id_bytes in self:
				del self.ids_to_objects[id]
				self.ids.remove(id)

	def get(self, needle):
		if hasattr(needle, 'id'):
			if needle not in self:
				return None
			return self.ids_to_objects[needle.id]
		try:
			id, id_bytes = parse_id(needle)
		except TypeError:
			return None
		except ValueError:
			return None
		else:
			if id in self:
				return self.ids_to_objects[id]
			return None

	def items(self):
		return self.ids_to_objects.items()

	def keys(self):
		return self.ids

	def values(self):
		objects = []
		for id in self.ids:
			objects.append(self.ids_to_objects[id])
		return objects
