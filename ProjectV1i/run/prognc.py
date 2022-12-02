import tail


t = tail.Tail('../nc.txt')

t.register_callback(exec)

t.follow(s=1)
