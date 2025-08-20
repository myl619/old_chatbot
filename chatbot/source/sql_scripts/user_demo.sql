USE chatbot;
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
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
GO
ALTER TABLE [dbo].[user_demo] ADD  CONSTRAINT [PK_user_demo] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
ALTER TABLE [dbo].[user_demo]  WITH CHECK ADD  CONSTRAINT [FK_user_demo_user_list] FOREIGN KEY([id])
REFERENCES [dbo].[user_list] ([id])
GO
ALTER TABLE [dbo].[user_demo] CHECK CONSTRAINT [FK_user_demo_user_list]
GO
BULK INSERT user_demo
FROM '/home/ubuntu/chatbot/csv_data/user_demo.csv'
WITH (
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO