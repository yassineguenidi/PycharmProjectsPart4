from PIL import Image
import streamlit as st
# Security
# passlib,hashlib,bcrypt,scrypt
import hashlib
# DB Management
import sqlite3



def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()

# DB  Functions
def create_usertable():
    if c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)'):
        return True
    else :
        return False


def add_userdata(username, password):
    if c.execute('INSERT INTO userstable(username,password) VALUES (?,?)', (username, password)):
        conn.commit()
        return True
    return False


def login_user(username, password):
    if c.execute('SELECT * FROM userstable WHERE username =? AND password = ?', (username, password)):
        data = c.fetchall()
        return data
    else :
        return False


def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

