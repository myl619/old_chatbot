USE chatbot;
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[lab_test_result](
	[id] [int] NOT NULL,
	[username] [varchar](max) NOT NULL,
	[lab_id] [int] NOT NULL,
	[test_item] [varchar](max) NOT NULL,
	[test_result] [float] NOT NULL,
	[test_dt] [datetime2](7) NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[lab_test_result] ADD  CONSTRAINT [PK_lab_test_result] PRIMARY KEY CLUSTERED 
(
	[lab_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
ALTER TABLE [dbo].[lab_test_result]  WITH CHECK ADD  CONSTRAINT [FK_lab_test_result_user_list] FOREIGN KEY([id])
REFERENCES [dbo].[user_list] ([id])
GO
ALTER TABLE [dbo].[lab_test_result] CHECK CONSTRAINT [FK_lab_test_result_user_list]
GO
BULK INSERT lab_test_result
FROM '\\home\\ubuntu\\chatbot\\csv_data\\lab_test_result.csv'
WITH (
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO
