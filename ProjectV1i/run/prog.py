import tail


t = tail.Tail('../network.txt')

t.register_callback(exec)

t.follow(s=1)
