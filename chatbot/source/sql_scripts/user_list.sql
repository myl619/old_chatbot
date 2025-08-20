USE chatbot;
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
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
GO
ALTER TABLE [dbo].[user_list] ADD  CONSTRAINT [PK_user_list] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
BULK INSERT user_list
FROM 'D:\S3\user_list.csv'
WITH (
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO


