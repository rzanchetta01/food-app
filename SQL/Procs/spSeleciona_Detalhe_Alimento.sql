CREATE PROCEDURE sp_Busca_Nome_Eng
(
	@food_name varchar(250)
)

as
	SET NOCOUNT ON
BEGIN
	SELECT fn.name_en_us from TbFood_Name fn
	WHERE fn.name_en_us like @food_name+'%'
END