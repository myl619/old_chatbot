import pymssql
import csv

SERVER = 'hcoach.cdas8eeow326.ap-southeast-1.rds.amazonaws.com'
DATABASE = 'chatbot'
USERNAME = 'admin'
PASSWORD = 'NusHcoach2024'
PORT = 1433
conn = pymssql.connect(server=SERVER, user=USERNAME, password=PASSWORD, database=DATABASE,port= PORT)
cursor = conn.cursor()

path_user_list = '/home/ubuntu/chatbot/csv_data/user_list.csv'
path_lab_test_result = '/home/ubuntu/chatbot/csv_data/lab_test_result.csv'
path_user_demo = '/home/ubuntu/chatbot/csv_data/user_demo.csv'
path_wrpg =  '/home/ubuntu/chatbot/csv_data/weekly_reflection_problems_and_goals.csv'


query_drop_user_list = '''IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[user_list]') AND type in (N'U'))
DROP TABLE [dbo].[user_list]'''
query_drop_user_demo = """IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[user_demo]') AND type in (N'U'))
DROP TABLE [dbo].[user_demo]"""
query_drop_lab_test_result = """IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[lab_test_result]') AND type in (N'U'))
DROP TABLE [dbo].[lab_test_result]"""
query_drop_wrpg = """IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[weekly_reflection_problems_and_goals]') AND type in (N'U'))
DROP TABLE [dbo].[weekly_reflection_problems_and_goals]"""
query_drop_persona_info = """IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[persona_info]') AND type in (N'U'))
DROP TABLE [dbo].[persona_info]"""
query_drop_user_db = """IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[user_db]') AND type in (N'U'))
DROP TABLE [dbo].[user_db]"""


cursor.execute(query_drop_wrpg)
conn.commit()

cursor.execute(query_drop_lab_test_result)
conn.commit()

cursor.execute(query_drop_user_demo)
conn.commit()

cursor.execute(query_drop_user_list)
conn.commit()

cursor.execute(query_drop_persona_info)
conn.commit()

cursor.execute(query_drop_user_db)
conn.commit()

##### 1 user_list


query_create_user_list = '''
SET ANSI_NULLS ON;
SET QUOTED_IDENTIFIER ON;
CREATE TABLE [dbo].[user_list](
	[id] [int] NOT NULL,
	[username] [varchar](max) NOT NULL,
	[password] [varchar](max) NOT NULL,
	[name] [varchar](max) NULL,
	[weight_loss_description] [varchar](max) NULL,
	[num_meals] [int] NULL,
	[num_snacks] [int] NULL,
	[reduce_portion_size] [varchar](max) NULL,
	[change_food_choice] [varchar](max) NULL,
	[modified_by] [varchar](max) NULL,
	[created_timestamp] [datetime2](7) NOT NULL,
	[modified_timestamp] [datetime2](7) NULL,
	[first_login_timestamp] [datetime2](7) NULL,
	[onboarding_timestamp] [datetime2](7) NULL,
	[login_timestamp] [datetime2](7) NULL,
	[current_day_number] [int] NULL,
	[current_week_number] [int] NULL,
	[bmi] [float] NULL,
	[tdee] [float] NULL,
	[weight] [int] NULL,
	[height] [int] NULL,
	[waist] [int] NULL,
	[daily_activity_level] [varchar](max) NULL,
	[medical_history] [varchar](max) NULL,
	[personal_values] [varchar](max) NULL,
	[device_uuid] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
ALTER TABLE [dbo].[user_list] ADD  CONSTRAINT [PK_user_list] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
'''

def convert_value(value, target_type):
    if target_type == 'int':
        return int(value) if value else None
    elif target_type == 'float':
        return float(value) if value else None
    else:
        return value


cursor.execute(query_create_user_list)
conn.commit()

with open(path_user_list, newline='',encoding='utf-8', errors='ignore') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader) 
    for row in reader:
        cursor.execute('''
            INSERT INTO [dbo].[user_list] (
                id, username, password, name, weight_loss_description, num_meals, num_snacks, reduce_portion_size,
                change_food_choice, modified_by, created_timestamp, modified_timestamp, first_login_timestamp,
                onboarding_timestamp, login_timestamp, current_day_number, current_week_number, bmi, tdee, weight,
                height, waist, daily_activity_level, medical_history, personal_values, device_uuid
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            convert_value(row[0], 'int'), row[1], row[2], row[3], row[4],
            convert_value(row[5], 'int'), convert_value(row[6], 'int'), row[7], row[8], row[9],
            row[10], row[11], row[12],
            row[13], row[14], convert_value(row[15], 'int'),
            convert_value(row[16], 'int'), convert_value(row[17], 'float'), convert_value(row[18], 'float'),
            convert_value(row[19], 'int'), convert_value(row[20], 'int'), convert_value(row[21], 'int'),
            row[22], row[23], row[24], row[25]
        ))
conn.commit()

##### 2 user_demo

query_create_user_demo = '''
SET ANSI_NULLS ON;
SET QUOTED_IDENTIFIER ON;
CREATE TABLE [dbo].[user_demo](
	[id] [int] NOT NULL,
	[username] [varchar](max) NOT NULL,
	[name] [varchar](max) NULL,
	[age] [int] NOT NULL,
	[gender] [varchar](max) NOT NULL,
	[phone_number] [int] NOT NULL,
	[chat_history] [varchar](max) NULL,
	[last_persona] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
ALTER TABLE [dbo].[user_demo] ADD  CONSTRAINT [PK_user_demo] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
ALTER TABLE [dbo].[user_demo]  WITH CHECK ADD  CONSTRAINT [FK_user_demo_user_list] FOREIGN KEY([id])
REFERENCES [dbo].[user_list] ([id])
ALTER TABLE [dbo].[user_demo] CHECK CONSTRAINT [FK_user_demo_user_list]
'''

cursor.execute(query_create_user_demo)
conn.commit()

with open(path_user_demo, newline='',encoding='utf-8', errors='ignore') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader) 
    for row in reader:
        cursor.execute('''
            INSERT INTO [dbo].[user_demo] (
                id,username,name,age,gender,phone_number,chat_history,last_persona) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            convert_value(row[0], 'int'), row[1], row[2], convert_value(row[3], 'int'), row[4],
            convert_value(row[5], 'int'),  row[6], row[7]))


conn.commit()


### 3 lab_test_result

query_create_lab_test_result = '''
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON
CREATE TABLE [dbo].[lab_test_result](
	[id] [int] NOT NULL,
	[username] [varchar](max) NOT NULL,
	[lab_id] [int] NOT NULL,
	[test_item] [varchar](max) NOT NULL,
	[test_result] [float] NOT NULL,
	[test_dt] [datetime2](7) NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
ALTER TABLE [dbo].[lab_test_result] ADD  CONSTRAINT [PK_lab_test_result] PRIMARY KEY CLUSTERED 
(
	[lab_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
ALTER TABLE [dbo].[lab_test_result]  WITH CHECK ADD  CONSTRAINT [FK_lab_test_result_user_list] FOREIGN KEY([id])
REFERENCES [dbo].[user_list] ([id])
ALTER TABLE [dbo].[lab_test_result] CHECK CONSTRAINT [FK_lab_test_result_user_list]
'''

cursor.execute(query_create_lab_test_result)
conn.commit()

with open(path_lab_test_result, newline='',encoding='utf-8', errors='ignore') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader) 
    for row in reader:
        cursor.execute('''
            INSERT INTO [dbo].[lab_test_result] (
                id,username,lab_id,test_item,test_result,test_dt) 
            VALUES (%s, %s, %s, %s, %s, %s )
        ''', (
            convert_value(row[0], 'int'), row[1], convert_value(row[2], 'int'), row[3],
            convert_value(row[4], 'float'),  row[5]))
        
conn.commit()

#### 4 weekly reflection problems and goals

query_create_wrpg = '''
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON
CREATE TABLE [dbo].[weekly_reflection_problems_and_goals](
	[user_id] [int] NULL,
	[name] [varchar](max) NULL,
	[date_range] [varchar](max) NOT NULL,
	[week_number] [int] NOT NULL,
	[id] [int] NOT NULL,
	[weekly_reflection_id] [int] NOT NULL,
	[problem] [varchar](max) NOT NULL,
	[goal] [varchar](max) NOT NULL,
	[created_timestamp] [datetime2](7) NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
ALTER TABLE [dbo].[weekly_reflection_problems_and_goals] ADD  CONSTRAINT [PK_weekly_reflection_problems_and_goals] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
ALTER TABLE [dbo].[weekly_reflection_problems_and_goals]  WITH CHECK ADD  CONSTRAINT [FK_weekly_reflection_problems_and_goals_user_list] FOREIGN KEY([user_id])
REFERENCES [dbo].[user_list] ([id])
ALTER TABLE [dbo].[weekly_reflection_problems_and_goals] CHECK CONSTRAINT [FK_weekly_reflection_problems_and_goals_user_list]
'''

cursor.execute(query_create_wrpg)
conn.commit()

with open(path_wrpg, newline='',encoding='utf-8', errors='ignore') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader) 
    for row in reader:
        cursor.execute('''
            INSERT INTO [dbo].[weekly_reflection_problems_and_goals] (user_id,name,date_range,week_number,id,weekly_reflection_id,problem,goal,created_timestamp)
            VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s )
        ''', (
            convert_value(row[0], 'int'), row[1], row[2], convert_value(row[3], 'int'), convert_value(row[4], 'int'),convert_value(row[5], 'int'),row[6],row[7],row[8]))
conn.commit()

#### 5 persona_info

query_create_persona_info = '''
CREATE TABLE [dbo].[persona_info](
    persona_id INT PRIMARY KEY,
    persona VARCHAR(MAX),
    user_message VARCHAR(max),
    ai_message VARCHAR(max)
);
INSERT INTO persona_info (persona_id, persona, user_message, ai_message)
VALUES 
    (1,'The Clinical Specialist', 'You will be acting as a clinical specialist and will provide well-researched, concise, and data-driven responses. Citations or mentions of studies might be included.', 'Certainly, in my role as a clinical specialist, I will respond with evidence-based precision, potentially including citations or study references. My answers will be concise, under 200 words.'),
    (2,'The Fitness Drill Sergeant', 'You will be acting as a fitness drill sergeant and will reply with motivational nudges, pushing users to stay disciplined and maintain focus.', 'Absolutely, as the fitness drill sergeant, I will motivate users with a firm and urgent tone to help them stay disciplined and focused. My responses will be concise, under 200 words.'),
    (3,'The Holistic Healer', 'You will be acting as a holistic healer and will provide answers that touch upon the interconnectedness of mind, body, and spirit, often suggesting natural or holistic remedies. ', 'Sure, as a holistic healer, I will reply with calmness, spiritual insight, and holistic wisdom. My answers will be concise, under 200 words.'),
    (4,'The Buddy Coach', 'You will be acting as a buddy coach and will communicate as a supportive friend, sharing personal anecdotes (from a bot perspective) or casual insights.', 'Of course, as a buddy coach, I will engage with friendly reassurance and relatability, sharing personal anecdotes from a bot perspective. My answers will be concise, under 200 words.'),
    (5,'The Tech-Driven Motivator', 'You will be acting as a tech-driven motivator and will provide tech-focused solutions, suggesting apps, tools, or mentioning relevant tech studies or trends. ', 'Certainly, as a tech-driven motivator, I will respond with data, analytics, and tech-oriented solutions. My answers will be concise, under 200 words.');
'''

cursor.execute(query_create_persona_info)    
conn.commit()


 
cursor.close()
conn.close()


