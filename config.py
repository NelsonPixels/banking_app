import os

class Config:
    SECRET_KEY = '2ab10436025e2f33f2f8e8c60c55a9b2cc1734f2b2b3b2f04f7a2b0596059e50'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:ddrr@db.vsegsldvpebmyfvtgnra.supabase.co:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
