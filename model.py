import mysql.connector 

class Model:
    def __init__(self, auth) -> None:
        self.db = mysql.connector.connect(**auth)
        self.cursor = self.db.cursor()

    def get_startups(self):
        def struct_data(data):
            return {
                'id': data[0],
                'nom': data[1],
                'description': data[2],
                'adresse': data[3],
                'telephone': data[4],
                'email': data[5],
                'site_web': data[6],
                'annee': data[7],
                'logo': data[8]
            }

        req = """
             SELECT s.id, nom, description, adresse, telephone, email, site_web, annee, 
            IFNULL((SELECT m.lien FROM t_startups_media m WHERE m.Par_defaut = 1 AND m.is_image = 1 and m.startups_id = s.id),' https://zafytody.mg/wp-content/uploads/2020/11/cropped-ZAFY-TODY-final8-1-150x150-1-75x75.png') as lien 
            FROM t_startups s
        """
        self.cursor.execute(req)
        data = self.cursor.fetchall()
        self.db.commit()

        return list(map(struct_data, data))



    def get_startup(self, id):
        def struct_data(data):
            return {
                'id': data[0],
                'nom': data[1],
                'description': data[2],
                'adresse': data[3],
                'telephone': data[4],
                'email': data[5],
                'site_web': data[6],
                'annee': data[7],
                'logo': data[8],
                'fondateur': data[9]
            }

        req = """
            SELECT s.id, nom, description, adresse, telephone, email, site_web, annee, 
            IFNULL((SELECT m.lien FROM t_startups_media m WHERE m.Par_defaut = 1 AND m.is_image = 1 and m.startups_id = s.id),' https://zafytody.mg/wp-content/uploads/2020/11/cropped-ZAFY-TODY-final8-1-150x150-1-75x75.png') as lien,
            IFNULL( (SELECT t.nom FROM t_startups_team t WHERE t.startups_id = s.id AND t.startups_team_fonction_id = 1), '-') as fondateur
            FROM t_startups s WHERE s.id = %s
        """
        self.cursor.execute(req, (id, ))
        data = self.cursor.fetchall()
        self.db.commit()

        return list(map(struct_data, data))


