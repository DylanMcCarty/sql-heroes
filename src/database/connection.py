import psycopg
from psycopg import OperationalError

def create_connection(db_name, db_user, db_password, db_host = "127.0.0.1", db_port = "5432"):
    connection = None
    try:
        connection = psycopg.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(query, params=None):
    connection = create_connection("postgres", "postgres", "postgres")
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print("Query executed successfully")
        connection.close()
        return cursor
    except OSError as e:
        print(f"The error '{e}' occurred or the hero name is already taken")

create_connection("postgres", "postgres", "postgres")

#DONT EDIT ABOVE THIS ====================================================================>


def login():
    print("""
 
        Please enter your name to login
        
        """)
    ans = input("------------ ")
    print("""

        Hello """ + ans + """ Welcome to Herobook, the website that
        allows you to fucking obliterate other heros from the
        comfort of your own home

        """)
    print("""
            
        
   ▄█    █▄       ▄████████    ▄████████  ▄██████▄  ▀█████████▄   ▄██████▄   ▄██████▄     ▄█   ▄█▄ 
  ███    ███     ███    ███   ███    ███ ███    ███   ███    ███ ███    ███ ███    ███   ███ ▄███▀ 
  ███    ███     ███    █▀    ███    ███ ███    ███   ███    ███ ███    ███ ███    ███   ███▐██▀   
 ▄███▄▄▄▄███▄▄  ▄███▄▄▄      ▄███▄▄▄▄██▀ ███    ███  ▄███▄▄▄██▀  ███    ███ ███    ███  ▄█████▀    
▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ███    ███ ▀▀███▀▀▀██▄  ███    ███ ███    ███ ▀▀█████▄    
  ███    ███     ███    █▄  ▀███████████ ███    ███   ███    ██▄ ███    ███ ███    ███   ███▐██▄   
  ███    ███     ███    ███   ███    ███ ███    ███   ███    ███ ███    ███ ███    ███   ███ ▀███▄ 
  ███    █▀      ██████████   ███    ███  ▀██████▀  ▄█████████▀   ▀██████▀   ▀██████▀    ███   ▀█▀ 
                              ███    ███                                                 ▀         

    
    """)
    question()

def question():
    print("""
    
        What would you like to do?
        
            1. Create a Hero?
        
            2. See Other Profiles?

            3. OBLITERATE THE EXISTENCE OF A BEING OTHER THAN YOURSELF

            4. Change Hero Alias, About Me, or Backstory
        
        """)
    ans = input("------------ ")
    if ans == "1":
        print("""
            
            What is your super Hero name?
            
            """)
        name = input("------------ ")
        print("""
        
            What\'s a short sentence about you?
            
            """)
        abtme = input("------------ ")
        print("""
        
            What\'s your backstory?
            
            """)
        bio = input("------------ ")
        print("""

            What\'s your super power?

            1. Super Strength

            2. Flying

            3. Telekenesis

            4. Telepathy

            5. Frost Breath

            6. Super Speed

            7. Super Vision

            """)
        power = input("------------ ")
        print("""

            New Hero Created!!!

            Name:
            """ + name + """

            About me:
            """ + abtme + """

            Biography:
            """ + bio + """

            """)
        if power == '1':
            print("""Ability: Super Strength
            
            """)
        if power == '2':
            print("""Ability: Flying
            
            """)
        if power == '3':
            print("""Ability: Telekenesis
            
            """)
        if power == '4':
            print("""Ability: Telepathy
            
            """)
        if power == '5':
            print("""Ability: Frost Breath
            
            """)
        if power == '6':
            print("""Ability: Super Speed
            
            """)
        if power == '7':
            print("""Ability: Super Vision
            
            """)
        query = """
            INSERT INTO heroes (name, about_me, biography)
            VALUES (%s, %s, %s)
        """
        query2 = """
            INSERT INTO abilities (hero_id, ability_type_id)
                SELECT
                    h.id,
                    a.id
                FROM heroes h
                JOIN abilities a ON a.id = %s
                WHERE name = %s
        """

        execute_query(query, (name, abtme, bio))
        execute_query(query2, (power, name))

    if ans == "2":
        print("""
        
            What would you like to see?
            
            1. All Superheros

            2. Look up a Superhero

            3. See SuperHero Friendships & Rivalries

            """)
        ans2 = input("------------ ")
    
        if ans2 == "1":
            query = """
                SELECT * FROM heroes
            """
            list_of_heroes = execute_query(query).fetchall()

            for record in list_of_heroes:
                print("""
                
                Name:
                """ + record[1] + """

                About Me:
                """ + record[2] + """

                Biography:
                """ + record[3] + """ 

                    """)
                
        if ans2 == "2":
            print("""
                
                Who would you like to look up?

                """)
            ans3 = input("------------ ")

            query = """
                SELECT * From Heroes
                Where Name =  %s
            """

            query2 = """
                SELECT 
                    ability_types.name
                FROM abilities
                INNER JOIN heroes ON abilities.hero_id=heroes.id
                INNER JOIN ability_types ON abilities.ability_type_id=ability_types.id
                WHERE heroes.name = %s
            """

            Hero = execute_query(query, (ans3,)).fetchone()
            Power = execute_query(query2, (ans3,)).fetchone()

            print("""
            
            Name:
            """ + Hero[1] + """

            About me:
            """ + Hero[2] + """

            Biography:
            """ + Hero[3] + """

            Power:
            """ + Power[0] + """

                """)

        if ans2 == "3":
            query = """
                SELECT 
                    h1.name,
                    h2.name,
                    rt.name
                FROM relationships r
                JOIN
                    heroes h1
                    ON r.hero1_id = h1.id
                JOIN 
                    heroes h2
                    ON r.hero2_id = h2.id
                JOIN 
                    relationship_types rt
                    ON r.relationship_type_id = rt.id
                """
            
            relationships = execute_query(query).fetchall()

            for relate in relationships:
                print("""

                """ + relate[0] + """ and """ + relate[1] + """ : """ + relate[2] + """

                """)

    if ans == "3":
        print("""
        
        WHO WOULD YOU LIKE TO MURDER?
        
        """)
        ans2 = input("------------ ")

        query = """

            DELETE FROM heroes 
            WHERE name = %s

        """
        print("""
        
        """ + ans2 + """ KILLED, OBLITERATED, MAIMED, TORTURED, NEVER TO COME BACK, YOURE HORRIBLE, YOU LOVE IT DON'T YOU? YOU SICK FREAK!!!

        THEY'VE BEEN 

                                                    
                                        ██ ▄█▀  ██▓ ██▓     ██▓    ▓█████ ▓█████▄ 
                                        ██▄█▒  ▓██▒▓██▒    ▓██▒    ▓█   ▀ ▒██▀ ██▌
                                        ▓███▄░ ▒██▒▒██░    ▒██░    ▒███   ░██   █▌
                                        ▓██ █▄ ░██░▒██░    ▒██░    ▒▓█  ▄ ░▓█▄   ▌
                                        ▒██▒ █▄░██░░██████▒░██████▒░▒████▒░▒████▓ 
                                        ▒ ▒▒ ▓▒░▓  ░ ▒░▓  ░░ ▒░▓  ░░░ ▒░ ░ ▒▒▓  ▒ 
                                        ░ ░▒ ▒░ ▒ ░░ ░ ▒  ░░ ░ ▒  ░ ░ ░  ░ ░ ▒  ▒ 
                                        ░ ░░ ░  ▒ ░  ░ ░     ░ ░      ░    ░ ░  ░ 
                                        ░  ░    ░      ░  ░    ░  ░   ░  ░   ░    
                                                                        ░      

                                                
        """)

        murder = execute_query(query, (ans2,))


    if ans == "4":
        print("""
        
            Which Hero are you trying to change?

        """)
        prop1 = input("")
        print("""
        
            Would you like to change Hero Alias, About Me, or Backstory?

            1. Hero Alias

            2. About me

            3. Backstory

        """)
        ans2 = input("------------ ")
        if ans2 == "1":
            print("""

                What would you like the new About Me to be?
            
            """)
            prop2= input("------------ ")

            query = """
                UPDATE heroes
                SET about_me = %s
                WHERE name = %s
            """

            bio = execute_query(query, (prop2, prop1))

            print("""
            
                About Me Changed

            """)
        if ans2 == "2":
            print("""

                What would you like the new Backstory to be?
            
            """)
            prop2= input("------------ ")

            query = """
                UPDATE heroes
                SET biography = %s
                WHERE name = %s
            """

            bio = execute_query(query, (prop2, prop1))

            print("""
            
                Backstory Changed

            """)
        if ans2 == "3":
            print("""

                What would you like the new Hero Alias to be?
            
            """)
            prop2= input("------------ ")

            query = """
                UPDATE heroes
                SET name = %s
                WHERE name = %s
            """

            bio = execute_query(query, (prop2, prop1))

            print("""
            
                Hero Alias Changed

            """)
    question()







login()




    # name = "Chill Woman"
    # query = """
    #     SELECT * from heroes
    #     WHERE name = %s
    # """

    # list_of_heroes = execute_query(query, (name,)).fetchall()
    # print(list_of_heroes)
    # # print(list_of_heroes[1])
    # # print(list_of_heroes[2])
    # # print(list_of_heroes[3])
    # print("")
    # for record in list_of_heroes:
    #     print("")
    #     print(record[1])
    #     print(record[2])
    #     print(record[3])
    #     print("")