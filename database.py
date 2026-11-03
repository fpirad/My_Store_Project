# import mysql.connector
# mydb = mysql.connector.connect(
#   host="127.0.0.1",
#   user="root",
#   password="",
#   database='appstore'
# )

# mycursor = mydb.cursor()
# mycursor.execute('''CREATE TABLE `appstore`.`customer` (`id` INT NOT NULL AUTO_INCREMENT ,
#                                                     `cname` VARCHAR(20) NOT NULL ,
#                                                     `age` INT NOT NULL ,
#                                                     `address` VARCHAR(50) NOT NULL ,
#                                                     `pic` VARCHAR(50) NOT NULL ,
#                                                     `mobile` VARCHAR(11) NOT NULL ,
#                                                     `active` INT NOT NULL DEFAULT '1' ,
#                                                     PRIMARY KEY (`id`)) ENGINE = MyISAM;')'''
# )

import sqlite3
import requests
import json

class DataBase():
    def __init__(self):
        self.mydb = sqlite3.connect('mydb.db')
        self.create_tables()

    ################################################################## Products 

    def create_products(self,name,price):
        data = {'name' : name , 'price': price}
        response = requests.post('http://127.0.0.1:8000/products/CreateProduct/' , json=data)
        if response.status_code == 200 :
            print(response.json())
        else:
            print(response.json() , response.status_code)

    # def create_products(self,name,price):
    #     mycursor = self.mydb.cursor()
    #     sql = "INSERT INTO products (pname, price) VALUES (?, ?)"
    #     val = (name,price)
    #     mycursor.execute(sql,val)
    #     self.mydb.commit()
    #     mycursor.close()

    def read_products(self):
        response = requests.get('http://127.0.0.1:8000/products/ReadAllProducts/')
        if response.status_code == 200 :
            return response.json()
        else:
            print(response.json() , response.status_code)

    # def read_products(self):
    #     mycursor = self.mydb.cursor()
    #     sql = "SELECT * FROM products"
    #     mycursor.execute(sql)
    #     data = mycursor.fetchall()
    #     mycursor.close()
    #     return data

    def read_products_by_id(self,id):
        response = requests.get(f'http://127.0.0.1:8000/products/ReadProductById/{id}/')
        if response.status_code == 200 :
            return response.json()
        else:
            print(response.json() , response.status_code)

    # def read_products_by_id(self,id):
    #     mycursor = self.mydb.cursor()
    #     sql = "SELECT * FROM products WHERE id =? "
    #     val = (id, )
    #     mycursor.execute(sql,val)
    #     data = mycursor.fetchone()
    #     mycursor.close()
    #     return data


    # def read_productName_by_id(self,id):
    #     mycursor = self.mydb.cursor()
    #     sql = "SELECT pname FROM products WHERE id =? "
    #     val = (id, )
    #     mycursor.execute(sql,val)
    #     data = mycursor.fetchone()
    #     mycursor.close()
    #     return data

    def update_products(self,id,name,price):
        data = {'id':id , 'name':name , 'price':price}
        response = requests.put('http://127.0.0.1:8000/products/UpdateProduct/' , json=data)
        if response.status_code == 200 :
            print(response.json())
        else:
            print(response.json() , response.status_code)


    # def update_products(self,id,name,price):
    #     mycursor = self.mydb.cursor()
    #     sql = "UPDATE products SET pname=? , price=? WHERE id =? "
    #     val =(name,price,id)
    #     mycursor.execute(sql,val)
    #     self.mydb.commit()
    #     mycursor.close()

    def delete_product(self,id):
        response = requests.delete(f'http://127.0.0.1:8000/products/DeleteProductbyId/{id}/')
        if response.status_code == 200 :
            print(response.json())
        else:
            print(response.json() , response.status_code)

    # def delete_product(self,id):
    #     mycursor = self.mydb.cursor()
    #     sql = "DELETE FROM products WHERE id=?"
    #     val = (id, )
    #     mycursor.execute(sql,val)
    #     self.mydb.commit()
    #     mycursor.close()

    def delete_all_products(self):
        response = requests.delete('http://127.0.0.1:8000/products/DeleteAllProducts/')
        if response.status_code == 200 :
            print(response.json())
        else:
            print(response.json() , response.status_code)

    # def delete_all_products(self):
    #     mycursor = self.mydb.cursor()
    #     sql = "DELETE FROM products"
    #     mycursor.execute(sql)
    #     self.mydb.commit()
    #     mycursor.close()

    ################################################################## Customers
    def create_customers(self,name,photo):
        data = {'username':name , 'pic': photo}
        response = requests.post(url='http://127.0.0.1:8000/customers/CreateCustomer/' , json = data)  # json = data   Or  data = json.dumps(data)
        if response.status_code==200:
            print(response.json())
        else:
            print(response.json()  ,response.status_code)

    # def create_customers(self,name,photo):
    #     mycursor = self.mydb.cursor()
    #     sql = "INSERT INTO customers (cname, photo) VALUES (?, ?)"
    #     val = (name,photo)
    #     mycursor.execute(sql,val)
    #     id = mycursor.lastrowid
    #     self.mydb.commit()
    #     mycursor.close()
    #     return id

    def read_customers(self):
        response = requests.get('http://127.0.0.1:8000/customers/ReadAllCustomers/')
        if response.status_code==200:
            return response.json()
        else:
            print('not ok')

    # def read_customers(self): 
        # mycursor = self.mydb.cursor()
        # sql = "SELECT * FROM customers"
        # mycursor.execute(sql)
        # data = mycursor.fetchall()
        # mycursor.close()
        # return data

    def read_customers_by_id(self,id):
        response = requests.get(f'http://127.0.0.1:8000/customers/ReadCustomerById/{id}/')
        if response.status_code == 200 :
            return response.json()
        else:
            print(response.json() , response.status_code)


    # def read_customers_by_name(self,name):
    #     mycursor = self.mydb.cursor()
    #     sql = "SELECT * FROM customers WHERE cname like ? "
    #     val = (f'%{name}%', )
    #     mycursor.execute(sql,val)
    #     data = mycursor.fetchall()
    #     mycursor.close()
    #     return data


    # def read_customers_by(self,id='',name=''):
    #     data = requests.get('http://127.0.0.1:8000/customers/ReadAllCustomers/')
    #     if data.status_code==200:
    #         return data.json()
    #     else:
    #         print('not ok')

    def read_customers_by(self,name:str='',id:int=None):
        # id=None if id=='' else int(id)
        data = {'username':name , 'id': None if id == '' else int(id)}
        response = requests.get('http://127.0.0.1:8000/customers/SearchCustomer/' , params=data)
        if response.status_code == 200 :
            return response.json()
        else:
            print(response.json() , response.status_code)
        return []


        # response = requests.get('http://127.0.0.1:8000/customers/ReadAllCustomers/')
        # if response.status_code==200:
        #     return response.json()   
        # else:
        #     print('moshkeli hast')
        # if name !='':
        #     response = requests.get(f'http://127.0.0.1:8000/customers/ReadCustomerByName/{name}/')
        #     if response.status_code==200:
        #         return response.json() 
        #     else:
        #         print(response.json() , response.status_code)
        # if id !='':
        #     response = requests.get(f'http://127.0.0.1:8000/customers/ReadCustomerById/{id}/')
        #     if response.status_code == 200 :
        #         return response.json()
        #     else:
        #         print(response.json() , response.status_code)

    # def read_customers_by(self,name,id):     
    #     sql = "SELECT * FROM customers WHERE 1=1 "
    #     val = tuple()
    #     if name !='':
    #         sql += 'AND cname LIKE ?'
    #         val += (f'%{name}%', )
    #     if id !='':
    #         sql += 'AND id=?'
    #         val += (id,)
    #     mycursor = self.mydb.cursor()
    #     mycursor.execute(sql,val)
    #     data = mycursor.fetchall()
    #     mycursor.close()
    #     return data

    # def read_customerPhoto_by_id(self,cid):
    #     mycursor = self.mydb.cursor()
    #     sql = "SELECT photo FROM customers WHERE id =? "
    #     val = (cid, )
    #     mycursor.execute(sql,val)
    #     data = mycursor.fetchone()
    #     mycursor.close()
    #     return data
    
    # def read_customerName_by_id(self,cid):
    #     mycursor = self.mydb.cursor()
    #     sql = "SELECT cname FROM customers WHERE id =? "
    #     val = (cid, )
    #     mycursor.execute(sql,val)
    #     data = mycursor.fetchone()
    #     mycursor.close()
    #     return data
        
    ################################################################## Factors  
    def create_factors(self,cid,total_amount,invoice_date=''):
        data = {'customer_id':cid ,'total':total_amount}
        response = requests.post('http://127.0.0.1:8000/factors/CreateFactor/',json=data)
        if response.status_code == 200 :
            # return response.json()
            return response.json()['id']
        else:
            print('create_factors have eror',response.json() , response.status_code)

    # def create_factors(self,cid,invoice_date,total_amount):
    #     sql = "INSERT INTO factors (cid, invoice_date, total_amount) VALUES (?, ?,?)"
    #     val = (cid, invoice_date, total_amount)
    #     mycursor = self.mydb.cursor()
    #     mycursor.execute(sql,val)
    #     self.mydb.commit()
    #     id = mycursor.lastrowid
    #     mycursor.close()
    #     return id

    def read_factors(self):
        response = requests.get('http://127.0.0.1:8000/factors/ReadAllFactors/')
        if response.status_code == 200 :
            return response.json()
        else:
            print('read_factors have eror',response.json() , response.status_code)

    # def read_factors(self):
    #     mycursor = self.mydb.cursor()
    #     sql = "SELECT * FROM factors"
    #     mycursor.execute(sql)
    #     data = mycursor.fetchall()
    #     mycursor.close()
    #     return data

    def read_factors_by(self,fid:int=None,cid:int=None,minPrice:int=None,maxPrice:int=None,minDate='',maxDate=''):
        data = {'fid':None if fid =='' else int(fid) ,'cid':None if cid =='' else int(cid),'minprice':None if minPrice =='' else int(minPrice),'maxprice':None if maxPrice =='' else int(maxPrice),'mindate':minDate,'maxdate':maxDate}
        response = requests.get('http://127.0.0.1:8000/factors/SearchFactor/',params=data)
        if response.status_code == 200 :
            return response.json()
        else:
            print('read_factors_by have eror',response.json() , response.status_code)
        return []


    # def read_factors_by(self,fid,cid,minPrice,maxPrice,minDate,maxDate):
    #     sql = "SELECT * FROM factors WHERE 1=1 "
    #     val = tuple()
    #     if cid !='':
    #         sql += 'AND cid=?'
    #         val += (cid, )
    #     if fid !='':
    #         sql += 'AND id=?'
    #         val += (fid,)
    #     if minPrice !='':
    #         sql += 'AND total_amount >= ?'
    #         val += (minPrice,)
    #     if maxPrice !='':
    #         sql += 'AND total_amount <= ?'
    #         val += (maxPrice,)
    #     if minDate !='':
    #         sql += 'AND invoice_date >= ?'
    #         val += (minDate,)
    #     if maxDate !='':
    #         sql += 'AND invoice_date <= ?'
    #         val += (maxDate,)
    #     sql += 'ORDER BY invoice_date'
    #     mycursor = self.mydb.cursor()
    #     mycursor.execute(sql,val)
    #     data = mycursor.fetchall()
    #     mycursor.close()
    #     return data 

    def update_factors(self,id,cid,invoice_date,total_amount):
        data = {'id':id,'customer_id':cid,'total':total_amount}
        response = requests.put('http://127.0.0.1:8000/factors/UpdateFactor/',json=data)
        if response.status_code == 200 :
            print(response.json())
        else:
            print('update_factors have eror',response.json() , response.status_code)

    # def update_factors(self,id,cid,invoice_date,total_amount):
    #     mycursor = self.mydb.cursor()
    #     sql = "UPDATE factors SET cid=?, invoice_date=? , total_amount=? WHERE id =? "
    #     val =(cid,invoice_date,total_amount,id)
    #     mycursor.execute(sql,val)
    #     self.mydb.commit()
    #     mycursor.close()

################################################################################## factor details

    def save_factor_details(self,factor_list):
        for i in factor_list:
            data = {'fid':i[0],'pid':i[1],'no':i[2],'price':i[3],'my_sum':i[4]}
            response = requests.post('http://127.0.0.1:8000/factoritems/CreateFactorItem/' , json=data)
        if response.status_code == 200 :
            return response.json()['id']
            # return response.json()
        else:
            print('save_factor_details have eror',response.json() , response.status_code)

      
    # def save_factor_details(self,factor_list):
    #     sql = "INSERT INTO invoice_details (fid,pid,price,quantity,total) VALUES (?,?,?,?,?)"
    #     val = factor_list  # list of tuples
    #     mycursor = self.mydb.cursor()
    #     mycursor.executemany(sql,val)
    #     self.mydb.commit()
    #     id = mycursor.lastrowid
    #     mycursor.close()
    #     return id
    
    # def save_factor_details(self,fid,pid,price,quantity,total):
    #     sql = "INSERT INTO invoice_details (fid,pid,price,quantity,total) VALUES (?,?,?,?,?)"
    #     val = (fid,pid,price,quantity,total)
    #     mycursor = self.mydb.cursor()
    #     mycursor.executemany(sql,val)
    #     self.mydb.commit()
    #     id = mycursor.lastrowid
    #     mycursor.close()
    #     return id

    # def update_factor_details(self,factor_list):
    #     mycursor = self.mydb.cursor()
    #     sql = "UPDATE invoice_details SET fid=?, pid=? , price=?, quantity=?, total=? WHERE id =? "
    #     val = factor_list
    #     mycursor.executemany(sql,val)
    #     self.mydb.commit()
    #     mycursor.close()

    # def update_factor_details(self,fid,pid,price,quantity,total):
    #     mycursor = self.mydb.cursor()
    #     sql = "UPDATE invoice_details SET fid=?, pid=? , price=?, quantity=?, total=? WHERE id =? "
    #     val = (fid,pid,price,quantity,total)
    #     mycursor.executemany(sql,val)
    #     self.mydb.commit()
    #     mycursor.close()

    def read_factor_details(self,fid):
        response = requests.get(f'http://127.0.0.1:8000/factoritems/ReadFactorItemByFid/{fid}/')
        if response.status_code == 200 :
            return response.json()
        else:
            print('read_factor_details have eror', response.json() , response.status_code)

    # def read_factor_details(self,fid):
    #     mycursor = self.mydb.cursor()
    #     sql = "SELECT * FROM invoice_details WHERE fid =? "
    #     val = (fid, )
    #     mycursor.execute(sql,val)
    #     data = mycursor.fetchall()
    #     mycursor.close()
    #     return data

    def delete_factor_details(self,fid:int):
        response =requests.delete(f'http://127.0.0.1:8000/factoritems/DeleteFactorItemByFid/{fid}/')
        if response.status_code == 200 :
            print(response.json())
        else:
            print('delete_factor_details have eror', response.json() , response.status_code)

    # def delete_factor_details(self,fid):
    #     mycursor = self.mydb.cursor()
    #     sql = "DELETE FROM invoice_details WHERE fid =? "
    #     val = (fid, )
    #     mycursor.execute(sql,val)
    #     self.mydb.commit()
    #     mycursor.close()

    ################################################################## create_tables
    
    def create_tables(self):
        mycursor = self.mydb.cursor()
        try:
            sql = '''
            CREATE TABLE customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cname TEXT NOT NULL,
                photo TEXT
            );
            '''
            mycursor.execute(sql)
            sql = '''
            CREATE TABLE products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pname TEXT NOT NULL,
                price INTEGER NOT NULL
            );'''
            mycursor.execute(sql)
            sql = '''
            CREATE TABLE factors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cid INTEGER NOT NULL,
                invoice_date TEXT NOT NULL,
                total_amount REAL NOT NULL DEFAULT 0,

                FOREIGN KEY (cid)
                    REFERENCES customers(id)
            );
            '''
            mycursor.execute(sql)
            sql = '''
            CREATE TABLE invoice_details (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fid INTEGER NOT NULL,
                pid INTEGER NOT NULL,
                price REAL NOT NULL,
                quantity REAL NOT NULL DEFAULT 1,
                total REAL NOT NULL DEFAULT 0,

                FOREIGN KEY (fid)
                    REFERENCES factors(id),

                FOREIGN KEY (pid)
                    REFERENCES products(id)
            );
            '''
            mycursor.execute(sql)
        except:
            pass
        finally:
            mycursor.close()


if __name__== '__main__':
    mydb = DataBase()
    mydb.delete_factor_details(1)
    # print(mydb.save_factor_details([{'fid':11,'pid':2,'price':200,'no':2, 'my_sum':400},{'fid':56,'pid':3,'price':400,'no':4, 'my_sum':10000}])['id'])
    # print(mydb.read_factor_details(2))
    # print(mydb.read_factors_by(cid=1,maxPrice=50000))
    # mydb.update_factors(id=4,cid=1,invoice_date='',total_amount=45000)
    # print(mydb.read_factors())
    # print(mydb.create_factors(cid=14,total_amount=2500))  #invoice_date=''
    # print(mydb.read_customers_by(id=2))
    # print(mydb.read_customers_by_id(11))
    # mydb.delete_product(10)
    # mydb.update_products(1,'nooshabehh' , '313000')
    # print(mydb.read_productName_by_id(22))
    # print(mydb.read_products_by_id(2))
    # print(mydb.read_products())
    # print(mydb.read_customers())
#     mydb.create_products('havij',200)
#     p = []
#     products = mydb.read_products()
#     for i in range(len(products)):
#         p.append({'id':products[i][0],'name':products[i][1],'price':products[i][2]})
#     print(p)
#     print(mydb.read_products_by_id(17))
    # print(mydb.read_factor_details(65))
#     print(mydb.read_factor_details(65)[2][1])
#     print(mydb.read_products_by_id(24))
#     print(mydb.read_products_by_id(24)[1])
#     print(mydb.read_productName_by_id(24)[0])
#     print(mydb.read_products)


