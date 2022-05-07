/****** BUSCA POR NOME DO ALIMENTO EM PTBR ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[sp_Busca_Nome_Ptbr]
(
	@food_name varchar(250)
)

as
	SET NOCOUNT ON
BEGIN
	SELECT fn.nome_pt_br from TbFood_Name fn
	WHERE fn.nome_pt_br like @food_name+'%'
END