from mysql.connector import connect

class DBConnector:
    def __init__(self):
        self.conn = connect(
            host='127.0.0.1',
            user='root',
            password='FullName5354',
        )
        database_name = 'wikiData_DB'
        query_db = f'CREATE DATABASE IF NOT EXISTS {database_name}'
        cursor = self.conn.cursor()
        cursor.execute(query_db)
        self.conn.commit()
        self.conn = connect(
            host='127.0.0.1',
            user='root',
            password='FullName5354',
            database='wikiData_DB'
        )
        self.cur = self.conn.cursor()
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS wikiData_TB (
                id INT AUTO_INCREMENT PRIMARY KEY,
                url VARCHAR(755),
                title VARCHAR(755),
                summary VARCHAR(755),
                discovery VARCHAR(755),
                composition VARCHAR(755),
                physical_attributes VARCHAR(755),
                other_information VARCHAR(755),
                title_two VARCHAR(755),
                summary_two VARCHAR(755),
                taharqo VARCHAR(755),
                the_statue VARCHAR(755),
                title_three VARCHAR(755),
                summary_three VARCHAR(755),
                the_british_museum_state VARCHAR(755),
                the_ashmolean_state VARCHAR(755)
            )
            """
        )
        self.conn.commit()

    def process_item(self, item, spider):
        def join_if_present(data):
            if data:
                return ', '.join(data)
            return None
        # Convert lists to strings
        item['title'] = join_if_present(item.get('title'))
        item['summary'] = join_if_present(item.get('summary'))
        item['discovery'] = join_if_present(item.get('discovery'))
        item['composition'] = join_if_present(item.get('composition'))
        item['physical_attributes'] = join_if_present(item.get('physical_attributes'))
        item['other_information'] = join_if_present(item.get('other_information'))
        item['title_two'] = join_if_present(item.get('title_two'))
        item['summary_two'] = join_if_present(item.get('summary_two'))
        item['taharqo'] = join_if_present(item.get('taharqo'))
        item['the_statue'] = join_if_present(item.get('the_statue'))
        item['title_three'] = join_if_present(item.get('title_three'))
        item['summary_three'] = join_if_present(item.get('summary_three'))
        item['the_british_museum_state'] = join_if_present(item.get('the_british_museum_state'))
        item['the_ashmolean_state'] = join_if_present(item.get('the_ashmolean_state'))

        # Your existing code to insert the data into the database
        self.cur.execute(
            """
            INSERT INTO wikiData_TB (
                url, 
                title, 
                summary, 
                discovery, 
                composition,
                physical_attributes,
                other_information,
                title_two,
                summary_two,
                taharqo,
                the_statue,
                title_three,
                summary_three,
                the_british_museum_state,
                the_ashmolean_state
            )
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                item['url'],
                item['title'],
                item['summary'],
                item['discovery'],
                item['composition'],
                item['physical_attributes'],
                item['other_information'],
                item['title_two'],
                item['summary_two'],
                item['taharqo'],
                item['the_statue'],
                item['title_three'],
                item['summary_three'],
                item['the_british_museum_state'],
                item['the_ashmolean_state']
            )
        )
        self.conn.commit()
        return item
    def close_spider(self, spider):
        self.conn.close()
        self.cur.close()