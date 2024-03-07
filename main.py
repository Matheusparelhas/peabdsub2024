import psycopg2

def conect_database(databe_name,user_name,host_name,pass_,port_name):
    com= psycopg2.connect(database = databe_name,
                          user= user_name,
                          host= host_name,
                          password = pass_,
                          port = port_name)
    return conn

if __name__ == '__name__':
    print("02")
    conn = conect_database("ticktcontroller","postgres", "localhost","pabd", 5432)

