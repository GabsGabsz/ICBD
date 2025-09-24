import sqlite3

conn = sqlite3.connect("dataBase/BD_ORIGIN.db")
cursor = conn.cursor()

Id_Keywords=[]
Id_Register_Null = []
# Exemplo de query
cursor.execute("SELECT pessoas_dom, dormitorio_dom, rendafamiliar, anosestudo_mae, escolaridade, anosestudo, dor_face, int_dor_face, autoavaliacao_nprot, autorrelato_implante, oidp1, oidp2, oidp3, oidp4, oidp5, oidp6, oidp7, oidp8, oidp9, dsup, coroa18, raiz18, pufa18, nt18, coroa17, raiz17, pufa17, nt17, coroa16, raiz16, pufa16, nt16, coroa15, raiz15, pufa15, nt15, coroa14, raiz14, pufa14, nt14, coroa13, raiz13, pufa13, nt13, coroa12, raiz12, pufa12, nt12, coroa11, raiz11, pufa11, nt11, coroa21, raiz21, pufa21, nt21, coroa22, raiz22, pufa22, nt22, coroa23, raiz23, pufa23, nt23, coroa24, raiz24, pufa24, nt24, coroa25, raiz25, pufa25, nt25, coroa26, raiz26, pufa26, nt26, coroa27, raiz27, pufa27, nt27, coroa28, raiz28, pufa28, nt28, dinf, coroa38, raiz38, pufa38, nt38, coroa37, raiz37, pufa37, nt37, coroa36, raiz36, pufa36, nt36, coroa35, raiz35, pufa35, nt35, coroa34, raiz34, pufa34, nt34, coroa33, raiz33, pufa33, nt33, coroa32, raiz32, pufa32, nt32, coroa31, raiz31, pufa31, nt31, coroa41, raiz41, pufa41, nt41, coroa42, raiz42, pufa42, nt42, coroa43, raiz43, pufa43, nt43, coroa44, raiz44, pufa44, nt44, coroa45, raiz45, pufa45, nt45, coroa46, raiz46, pufa46, nt46, coroa47, raiz47, pufa47, nt47, coroa48, raiz48, pufa48, nt48, trauma12, trauma11, trauma21, trauma22, trauma32, trauma31, trauma41, trauma42, ss_sd, calc_sd, bolsa_sd, pip_sd, ss_sc, calc_sc, bolsa_sc, pip_sc, ss_se, calc_se, bolsa_se, pip_se, ss_ie, calc_ie, bolsa_ie, pip_ie, ss_ic, calc_ic, bolsa_ic, pip_ic, ss_id, calc_id, bolsa_id, pip_id, usa_apal_orto, dai1, dai2, dai3, dai4, dai5, dai6, dai7, dai8, dai9, dai10, dai11, usoprotsup, necprotsup, usoprotinf, necprotinf, necsup_parcial_total, necinf_parcial_total, necprot, cariado, cariado_total, perdido, restaurado_com_carie, restaurado_sem_carie, higidos, cpod, pufa_prev_permanente, pufa_total_permanente_5a, pufa_envolvpulpar_permanente_5a, pufa_ulceracao_permanente_5a, pufa_fistula_permanente_5a, pufa_abscesso_permanente_5a, raiz_higida, raiz_cariada, raiz_cariada_total, raiz_rest_cariada, raiz_rest, raiz_implante, raiz_exposta, raiz_nao_exposta, raiz_excluida, nenhumtrauma, fraturatratada, fraturaesmalte, fraturaesmalte_dentina, envolvpulpar, perdatrauma, outrosdanos, prevtrauma, qqtrauma, nsextantes_semsangramento, nsextantes_sangramento, nsextantes_ssexcluidos, nsextantes_semcalculo, nsextantes_comcalculo, nsextantes_calcexcluido, nsextantes_bolsahigido, nsextantes_bolsarasa, nsextantes_bolsaprofunda, nsextantes_bolsaexcluidos, nsextantes_pip0, nsextantes_pip1, nsextantes_pip2, nsextantes_pip3, nsextantes_pip4, nsextantes_pip9, cpi, pip, prevss, prevcalc, prevbolsarasa, prevbolsaprofunda, dai, catdai, edentulismo, sm, rendapercapita FROM minha_tabela WHERE codigo = 122;")
# Mostrar resultados
for row in cursor.fetchall():
    print(row)

print("----------------------------------------------------------------------------------------------------------------------------")
print ("Colunas na tabela 'minha_tabela':")
print(Id_Keywords)
conn.close()
