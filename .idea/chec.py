class Movies:
    def __init__(self):
        self.name = []

    def __len__(self):
        return len(self.name)
    def __getitem__(self, i):
        return self.name[i]
    def __str__(self):
        return f'Movies with {self.name}'
    def __repr__(self):
        return f'Movies with {len(self)}'


data = Movies()
data.name.append('werdd')
data.name.append('ddlj')

print(data)

