USE chatbot;
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
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
GO
ALTER TABLE [dbo].[weekly_reflection_problems_and_goals] ADD  CONSTRAINT [PK_weekly_reflection_problems_and_goals] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
ALTER TABLE [dbo].[weekly_reflection_problems_and_goals]  WITH CHECK ADD  CONSTRAINT [FK_weekly_reflection_problems_and_goals_user_list] FOREIGN KEY([user_id])
REFERENCES [dbo].[user_list] ([id])
GO
ALTER TABLE [dbo].[weekly_reflection_problems_and_goals] CHECK CONSTRAINT [FK_weekly_reflection_problems_and_goals_user_list]
GO
BULK INSERT weekly_reflection_problems_and_goals
FROM '/home/ubuntu/chatbot/csv_data/weekly_reflection_problems_and_goals.csv'
WITH (
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO
