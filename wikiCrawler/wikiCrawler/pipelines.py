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
            CREATE TABLE IF NOT EXISTS wiki_TAB (
                id INT AUTO_INCREMENT PRIMARY KEY,
                url TEXT(755),
                title TEXT(755),
                summary TEXT(755),
                discovery TEXT(755),
                composition TEXT(755),
                physical_attributes TEXT(755),
                other_information TEXT(755),
                title_two TEXT(555),
                summary_two TEXT(755),
                taharqo TEXT(755),
                the_statue TEXT(755),
                title_three TEXT(755),
                summary_three TEXT(755),
                the_british_museum_state TEXT(755),
                the_ashmolean_state TEXT(755),
                title_four TEXT(755),
                summary_four TEXT(755),
                Broad_Street TEXT(755),
                Beaumont_Street TEXT(755),
                Beaumont_Street_2 TEXT(755),
                Beaumont_Street_3 TEXT(755),
                Beaumont_Street_4 TEXT(755),
                Beaumont_Street_5 TEXT(755),
                Renovations TEXT(755),
                Renovations_2 TEXT(755),
                Renovations_3 TEXT(755),
                Renovations_4 TEXT(755),
                Renovations_5 TEXT(755),
                Renovations_6 TEXT(755),
                Collections TEXT(755),
                title_five TEXT(755),
                summary_five TEXT(755),
                summary_five2 TEXT(755),
                summary_five3 TEXT(755),
                Naming_Conventions TEXT(755),
                Naming_Conventions_2 TEXT(755),
                Naming_Conventions_3 TEXT(755),
                Sources TEXT(755),
                Sources_2 TEXT(755),
                Sources_3 TEXT(755),
                Sources_4 TEXT(755),
                Contents TEXT(755),
                Contents_2 TEXT(755),
                Contents_3 TEXT(755),
                Before_the_Flood TEXT(755),
                Before_the_Flood_2 TEXT(755),
                First_Dynasty_of_Kish_to_Lugal_zage_si TEXT(755),
                First_Dynasty_of_Kish_to_Lugal_zage_si_2 TEXT(755),
                First_Dynasty_of_Kish_to_Lugal_zage_si_3 TEXT(755),
                First_Dynasty_of_Kish_to_Lugal_zage_si_4 TEXT(755),
                Akkad_to_Isin TEXT(755),
                Akkad_to_Isin_2 TEXT(755),
                Sumerian_King_Summary_title TEXT(755),
                Sumerian_King_Summary TEXT(755),
                Discussion TEXT(755),
                Discussion_2 TEXT(755),
                Dating_reaction_and_purpose TEXT(755),
                Dating_reaction_and_purpose_2 TEXT(755),
                Dating_reaction_and_purpose_3 TEXT(755),
                Reliability_of_Source TEXT(755),
                Reliability_of_Source_2 TEXT(755),
                Reliability_of_Source_3 TEXT(755),
                Reliability_of_Source_4 TEXT(755),
                Reliability_of_Source_5 TEXT(755),
                Reliability_of_Source_6 TEXT(755),
                Antediluvian_rulers TEXT(755),
                title_six TEXT(755),
                summary_six TEXT(755),
                summary_six2 TEXT(755),
                summary_six3 TEXT(755),
                Flood_Myth TEXT(755),
                Flood_Myth_2 TEXT(755),
                Flood_Myth_3 TEXT(755),
                Flood_Myth_4 TEXT(755),
                Flood_Myth_5 TEXT(755),
                Flood_Myth_6 TEXT(755),
                Flood_Myth_7 TEXT(755),
                Parallels TEXT(755),
                Parallels_2 TEXT(755),
                Ziusudra_and_Xisuthros TEXT(755),
                Ziusudra_and_Xisuthros_2 TEXT(755),
                Ziusudra_and_Xisuthros_3 TEXT(755),
                Ziusudra_and_Xisuthros_4 TEXT(755),
                title_seven TEXT(755),
                summary_seven TEXT(755),
                Creation_Myths TEXT(755),
                Creation_Myths2 TEXT(755),
                Atra_Hasis TEXT(755),
                Atra_Hasis_2 TEXT(755),
                Eridu_Genesis TEXT(755),
                Eridu_Genesis_2 TEXT(755),
                Enuma_Elish TEXT(755),
                Enuma_Elish_2 TEXT(755),
                Heroic_epics TEXT(755),
                Heroic_epics_2 TEXT(755),
                The_Myth_of_Adapa TEXT(755),
                The_Myth_of_Adapa_2 TEXT(755),
                Common_Themes TEXT(755),
                Common_Themes_2 TEXT(755),
                Common_Themes_3 TEXT(755),
                Common_Themes_4 TEXT(755),
                Common_Themes_5 TEXT(755),
                Sources_Mesopotamian_Myths TEXT(755),
                Sources_Mesopotamian_Myths_2 TEXT(755)
                )
            """
        )
        self.conn.commit()

    def process_item(self, item, spider):
        def join_if_present(data):
            if data:
                return ', '.join(data)
            return None
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
        item['title_four']= join_if_present(item.get('title_four'))
        item['summary_four']= join_if_present(item.get('summary_four'))
        item['Broad_Street']= join_if_present(item.get('Broad_Street'))
        item['Beaumont_Street']= join_if_present(item.get('Beaumont_Street'))
        item['Beaumont_Street_2']= join_if_present(item.get('Beaumont_Street_2'))
        item['Beaumont_Street_3']= join_if_present(item.get('Beaumont_Street_3'))
        item['Beaumont_Street_4']= join_if_present(item.get('Beaumont_Street_4'))
        item['Beaumont_Street_5']= join_if_present(item.get('Beaumont_Street_5'))
        item['Renovations']= join_if_present(item.get('Renovations'))
        item['Renovations_2']= join_if_present(item.get('Renovations_2'))
        item['Renovations_3']= join_if_present(item.get('Renovations_3'))
        item['Renovations_4']=join_if_present(item.get('Renovations_4'))
        item['Renovations_5']= join_if_present(item.get('Renovations_5'))
        item['Renovations_6']= join_if_present(item.get('Renovations_6'))
        item['Collections']= join_if_present(item.get('Collections'))
        item['title_five']= join_if_present(item.get('title_five'))
        item['summary_five']= join_if_present(item.get('summary_five'))
        item['summary_five2']= join_if_present(item.get('summary_five2'))
        item['summary_five3']= join_if_present(item.get('summary_five3'))
        item['Naming_Conventions']= join_if_present(item.get('Naming_Conventions'))
        item['Naming_Conventions_2']= join_if_present(item.get('Naming_Conventions_2'))
        item['Naming_Conventions_3']= join_if_present(item.get('Naming_Conventions_3'))
        item['Sources']= join_if_present(item.get('Sources'))
        item['Sources_2']= join_if_present(item.get('Sources_2'))
        item['Sources_3']= join_if_present(item.get('Sources_3'))
        item['Sources_4']= join_if_present(item.get('Sources_4'))
        item['Contents']= join_if_present(item.get('Contents'))
        item['Contents_2']= join_if_present(item.get('Contents_2'))
        item['Contents_3']= join_if_present(item.get('Contents_3'))
        item['Before_the_Flood']= join_if_present(item.get('Before_the_Flood'))
        item['Before_the_Flood_2']= join_if_present(item.get('Before_the_Flood_2'))
        item['First_Dynasty_of_Kish_to_Lugal_zage_si']= join_if_present(item.get('First_Dynasty_of_Kish_to_Lugal_zage_si'))
        item['First_Dynasty_of_Kish_to_Lugal_zage_si_2']= join_if_present(item.get('First_Dynasty_of_Kish_to_Lugal_zage_si_2'))
        item['First_Dynasty_of_Kish_to_Lugal_zage_si_3']= join_if_present(item.get('First_Dynasty_of_Kish_to_Lugal_zage_si_3'))
        item['First_Dynasty_of_Kish_to_Lugal_zage_si_4']= join_if_present(item.get('First_Dynasty_of_Kish_to_Lugal_zage_si_4'))
        item['Akkad_to_Isin']= join_if_present(item.get('Akkad_to_Isin'))
        item['Akkad_to_Isin_2']= join_if_present(item.get('Akkad_to_Isin_2'))
        item['Sumerian_King_Summary_title']= join_if_present(item.get('Sumerian_King_Summary_title'))
        item['Sumerian_King_Summary']= join_if_present(item.get('Sumerian_King_Summary'))
        item['Discussion']= join_if_present(item.get('Discussion'))
        item['Discussion_2']= join_if_present(item.get('Discussion_2'))
        item['Dating_reaction_and_purpose']= join_if_present(item.get('Dating_reaction_and_purpose'))
        item['Dating_reaction_and_purpose_2']= join_if_present(item.get('Dating_reaction_and_purpose_2'))
        item['Dating_reaction_and_purpose_3']= join_if_present(item.get('Dating_reaction_and_purpose_3'))
        item['Reliability_of_Source']= join_if_present(item.get('Reliability_of_Source'))
        item['Reliability_of_Source_2']= join_if_present(item.get('Reliability_of_Source_2'))        
        item['Reliability_of_Source_3']= join_if_present(item.get('Reliability_of_Source_3'))
        item['Reliability_of_Source_4']= join_if_present(item.get('Reliability_of_Source_4'))
        item['Reliability_of_Source_5']= join_if_present(item.get('Reliability_of_Source_5'))
        item['Reliability_of_Source_6']= join_if_present(item.get('Reliability_of_Source_6'))
        item['Antediluvian_rulers']= join_if_present(item.get('Antediluvian_rulers'))
        item['title_six']= join_if_present(item.get('title_six'))
        item['summary_six']= join_if_present(item.get('summary_six'))
        item['summary_six2']= join_if_present(item.get('summary_six2'))
        item['summary_six3']= join_if_present(item.get('summary_six3'))
        item['Flood_Myth']= join_if_present(item.get('Flood_Myth'))
        item['Flood_Myth_2']= join_if_present(item.get('Flood_Myth_2'))
        item['Flood_Myth_3']= join_if_present(item.get('Flood_Myth_3'))
        item['Flood_Myth_4']= join_if_present(item.get('Flood_Myth_4'))
        item['Flood_Myth_5']= join_if_present(item.get('Flood_Myth_5'))
        item['Flood_Myth_6']= join_if_present(item.get('Flood_Myth_6'))
        item['Flood_Myth_7']= join_if_present(item.get('Flood_Myth_7'))
        item['Parallels']= join_if_present(item.get('Parallels'))
        item['Parallels_2']= join_if_present(item.get('Parallels_2'))
        item['Ziusudra_and_Xisuthros']= join_if_present(item.get('Ziusudra_and_Xisuthros'))
        item['Ziusudra_and_Xisuthros_2']= join_if_present(item.get('Ziusudra_and_Xisuthros_2'))
        item['Ziusudra_and_Xisuthros_3']= join_if_present(item.get('Ziusudra_and_Xisuthros_3'))
        item['Ziusudra_and_Xisuthros_4']= join_if_present(item.get('Ziusudra_and_Xisuthros_4'))
        item['title_seven']= join_if_present(item.get('title_seven'))
        item['summary_seven']= join_if_present(item.get('summary_seven'))
        item['Creation_Myths']= join_if_present(item.get('Creation_Myths'))
        item['Creation_Myths2']= join_if_present(item.get('Creation_Myths2'))
        item['Atra_Hasis']= join_if_present(item.get('Atra_Hasis'))
        item['Atra_Hasis_2']= join_if_present(item.get('Atra_Hasis_2'))
        item['Eridu_Genesis']= join_if_present(item.get('Eridu_Genesis'))
        item['Eridu_Genesis_2']= join_if_present(item.get('Eridu_Genesis_2'))
        item['Enuma_Elish']= join_if_present(item.get('Enuma_Elish'))
        item['Enuma_Elish_2']= join_if_present(item.get('Enuma_Elish_2'))
        item['Heroic_epics']= join_if_present(item.get('Heroic_epics'))
        item['Heroic_epics_2']= join_if_present(item.get('Heroic_epics_2'))
        item['The_Myth_of_Adapa']= join_if_present(item.get('The_Myth_of_Adapa'))
        item['The_Myth_of_Adapa_2']= join_if_present(item.get('The_Myth_of_Adapa_2'))
        item['Common_Themes']= join_if_present(item.get('Common_Themes'))
        item['Common_Themes_2']= join_if_present(item.get('Common_Themes_2'))
        item['Common_Themes_3']= join_if_present(item.get('Common_Themes_3'))
        item['Common_Themes_4']= join_if_present(item.get('Common_Themes_4'))
        item['Common_Themes_5']= join_if_present(item.get('Common_Themes_5'))
        item['Sources_Mesopotamian_Myths']= join_if_present(item.get('Sources_Mesopotamian_Myths'))
        item['Sources_Mesopotamian_Myths_2']= join_if_present(item.get('Sources_Mesopotamian_Myths_2'))

        self.cur.execute(
            """
            INSERT INTO wiki_TAB (
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
                the_ashmolean_state,
                title_four,
                summary_four,
                Broad_Street,
                Beaumont_Street,
                Beaumont_Street_2,
                Beaumont_Street_3,
                Beaumont_Street_4,
                Beaumont_Street_5,
                Renovations,
                Renovations_2,
                Renovations_3,
                Renovations_4,
                Renovations_5,
                Renovations_6,
                Collections,
                title_five,
                summary_five,
                summary_five2,
                summary_five3,
                Naming_Conventions,
                Naming_Conventions_2,
                Naming_Conventions_3,
                Sources,
                Sources_2,
                Sources_3,
                Sources_4,
                Contents,
                Contents_2,
                Contents_3,
                Before_the_Flood,
                Before_the_Flood_2,
                First_Dynasty_of_Kish_to_Lugal_zage_si,
                First_Dynasty_of_Kish_to_Lugal_zage_si_2,
                First_Dynasty_of_Kish_to_Lugal_zage_si_3,
                First_Dynasty_of_Kish_to_Lugal_zage_si_4,
                Akkad_to_Isin,
                Akkad_to_Isin_2,
                Sumerian_King_Summary_title,
                Sumerian_King_Summary,
                Discussion,
                Discussion_2,
                Dating_reaction_and_purpose,
                Dating_reaction_and_purpose_2,
                Dating_reaction_and_purpose_3,
                Reliability_of_Source,
                Reliability_of_Source_2,
                Reliability_of_Source_3,
                Reliability_of_Source_4,
                Reliability_of_Source_5,
                Reliability_of_Source_6,
                Antediluvian_rulers,
                title_six,
                summary_six,
                summary_six2,
                summary_six3,
                Flood_Myth,
                Flood_Myth_2,
                Flood_Myth_3,
                Flood_Myth_4,
                Flood_Myth_5,
                Flood_Myth_6,
                Flood_Myth_7,
                Parallels,
                Parallels_2,
                Ziusudra_and_Xisuthros,
                Ziusudra_and_Xisuthros_2,
                Ziusudra_and_Xisuthros_3,
                Ziusudra_and_Xisuthros_4,
                title_seven,
                summary_seven,
                Creation_Myths,
                Creation_Myths2,
                Atra_Hasis,
                Atra_Hasis_2,
                Eridu_Genesis,
                Eridu_Genesis_2,
                Enuma_Elish,
                Enuma_Elish_2,
                Heroic_epics,
                Heroic_epics_2,
                The_Myth_of_Adapa,
                The_Myth_of_Adapa_2,
                Common_Themes,
                Common_Themes_2,
                Common_Themes_3,
                Common_Themes_4,
                Common_Themes_5,
                Sources_Mesopotamian_Myths,
                Sources_Mesopotamian_Myths_2

            )
            VALUES(
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s)
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
                    item['the_ashmolean_state'],
                    item['title_four'],
                    item['summary_four'],
                    item['Broad_Street'],
                    item['Beaumont_Street'],
                    item['Beaumont_Street_2'],
                    item['Beaumont_Street_3'],
                    item['Beaumont_Street_4'],
                    item['Beaumont_Street_5'],
                    item['Renovations'],
                    item['Renovations_2'],
                    item['Renovations_3'],
                    item['Renovations_4'],
                    item['Renovations_5'],
                    item['Renovations_6'],
                    item['Collections'],
                    item['title_five'],
                    item['summary_five'],
                    item['summary_five2'],
                    item['summary_five3'],
                    item['Naming_Conventions'],
                    item['Naming_Conventions_2'],
                    item['Naming_Conventions_3'],
                    item['Sources'],
                    item['Sources_2'],
                    item['Sources_3'],
                    item['Sources_4'],
                    item['Contents'],
                    item['Contents_2'],
                    item['Contents_3'],
                    item['Before_the_Flood'],
                    item['Before_the_Flood_2'],
                    item['First_Dynasty_of_Kish_to_Lugal_zage_si'],
                    item['First_Dynasty_of_Kish_to_Lugal_zage_si_2'],
                    item['First_Dynasty_of_Kish_to_Lugal_zage_si_3'],
                    item['First_Dynasty_of_Kish_to_Lugal_zage_si_4'],
                    item['Akkad_to_Isin'],
                    item['Akkad_to_Isin_2'],
                    item['Sumerian_King_Summary_title'],
                    item['Sumerian_King_Summary'],
                    item['Discussion'],
                    item['Discussion_2'],
                    item['Dating_reaction_and_purpose'],
                    item['Dating_reaction_and_purpose_2'],
                    item['Dating_reaction_and_purpose_3'],
                    item['Reliability_of_Source'],
                    item['Reliability_of_Source_2'],
                    item['Reliability_of_Source_3'],
                    item['Reliability_of_Source_4'],
                    item['Reliability_of_Source_5'],
                    item['Reliability_of_Source_6'],
                    item['Antediluvian_rulers'],
                    item['title_six'],
                    item['summary_six'],
                    item['summary_six2'],
                    item['summary_six3'],
                    item['Flood_Myth'],
                    item['Flood_Myth_2'],
                    item['Flood_Myth_3'],
                    item['Flood_Myth_4'],
                    item['Flood_Myth_5'],
                    item['Flood_Myth_6'],
                    item['Flood_Myth_7'],
                    item['Parallels'],
                    item['Parallels_2'],
                    item['Ziusudra_and_Xisuthros'],
                    item['Ziusudra_and_Xisuthros_2'],
                    item['Ziusudra_and_Xisuthros_3'],
                    item['Ziusudra_and_Xisuthros_4'],
                    item['title_seven'],
                    item['summary_seven'],
                    item['Creation_Myths'],
                    item['Creation_Myths2'],
                    item['Atra_Hasis'],
                    item['Atra_Hasis_2'],
                    item['Eridu_Genesis'],
                    item['Eridu_Genesis_2'],
                    item['Enuma_Elish'],
                    item['Enuma_Elish_2'],
                    item['Heroic_epics'],
                    item['Heroic_epics_2'],
                    item['The_Myth_of_Adapa'],
                    item['The_Myth_of_Adapa_2'],
                    item['Common_Themes'],
                    item['Common_Themes_2'],
                    item['Common_Themes_3'],
                    item['Common_Themes_4'],
                    item['Common_Themes_5'],
                    item['Sources_Mesopotamian_Myths'],
                    item['Sources_Mesopotamian_Myths_2']
            )
        )
        self.conn.commit()
        return item
    def close_spider(self, spider):
        self.conn.close()
        self.cur.close()