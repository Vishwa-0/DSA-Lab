class SocialNetwork:
    def __init__(self, n):
        self.n = n
        self.matrix = [[0]*n for _ in range(n)]
        self.adj_list = [[] for _ in range(n)]

    def add_connection(self, user1, user2):
        self.matrix[user1][user2] = 1
        self.matrix[user2][user1] = 1
        self.adj_list[user1].append(user2)
        self.adj_list[user2].append(user1)

    def display_network(self):
        print("\nAdjacency Matrix:")
        for row in self.matrix:
            print(row)
        
        print("\nAdjacency List:")
        for i in range(self.n):
            print(f"User {i}: {self.adj_list[i]}")

    def check_connection(self, user1, user2):
        matrix_result = self.matrix[user1][user2] == 1
        list_result = user2 in self.adj_list[user1]
        print(f"\nConnection between User {user1} and User {user2}:")
        print(f"Matrix representation: {'Connected' if matrix_result else 'Not connected'}")
        print(f"List representation: {'Connected' if list_result else 'Not connected'}")

def main():
    n = int(input("Enter total number of users: "))
    network = SocialNetwork(n)
    
    edges = int(input("Enter number of connections: "))
    print("Enter connections (user1 user2):")
    for _ in range(edges):
        u1, u2 = map(int, input().split())
        network.add_connection(u1, u2)
    
    network.display_network()
    
    while True:
        print("\nCheck connection between users? (y/n)")
        if input().lower() != 'y':
            break
        u1, u2 = map(int, input("Enter two users to check connection: ").split())
        network.check_connection(u1, u2)

if __name__ == "__main__":
    main()
