from flask import Flask, request, render_template
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

app = Flask(__name__, template_folder=os.path.abspath('templates'))
engine = create_engine(
    os.getenv("DATABASE_URI")
)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    content = Column(String)

Base.metadata.create_all(engine)

@app.route('/', methods=['POST', 'GET'])
def add_message():
    if request.method == 'POST':
        content = request.form['content']
        session = Session()
        message = Message(content=content)
        session.add(message)
        session.commit()
        session.close()
        return 'Message added: {}'.format(content)
    else:
        return render_template('index.html')

@app.route('/messages', methods=['GET'])
def get_messages():
    session = Session()
    messages = session.query(Message).all()
    session.close()
    return {'messages': [{'id': message.id, 'content': message.content} for message in messages]}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)