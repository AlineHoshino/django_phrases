# Welcome to the phrases aplication! 🥰

This is a project with the objective of learning django. The heart of this project is the CRUD. 
You can signup,login, so you have access to your motivacional phrases.
I chose to do an app about motivacional phrases because if you are sad. you can use this app to write phrases that you like, and you can read it, and I hope your day become more happy!😊


##  API Documentation

#### Returns all items

```http
  GET /smart/notes
```

#### Returns one item

```http
  GET /smart/notes/${id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Mandatory**. ID item |

#### Create the item

```http
  POST /smart/notes/new
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `Title`      | `string` | **Title of the phrase** |
| `Text`      | `string` | **The phrase** |
| `author`      | `string` | **Author of the phrase** it has a default parameter-Anonymus|


#### Delete one item

```http
  DELETE /smart/notes/${id}/delete
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Mandatory**. ID item |


#### Update one item

```http
  POST /smart/notes/${id}/edit
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Mandatory**. ID item |


#### Signup

```http
  POST /signup
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `username`      | `string` | **like a nickname** |
| `password`      | `string` | **your password** |


## Reference

 - [Django Essential Training](https://www.linkedin.com/learning/django-essential-training)



## Learnings
I learned many things in this project. This project is based on the course Django Essential Training. This course was amazing.
I learned Django is a fast framework, it is in Python.
Django bases is MVT - Model-View-Template.
Model contains the dates of the apllication. This is the layer to manipulate, add and delete data.
View- receives request and send a response.
Template- everything the user can see.


## Stacks

Django and Python


## Running locally

1. Clone the projet

```bash
  git clone git@github.com:AlineHoshino/django_test.git
```

2. Enter the project directory

```bash
  cd django_test
```

3. Create your virtual env
```
python3 -m venv .venv
```
2. Active the venv
```
source .venv/bin/activate
```
3. Install the dependences
```
python3 -m pip install -r requirements.txt
```
4. Run the server
```
python3 manage.py runserver
```


