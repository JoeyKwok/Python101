BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "DNS Join" (
	"tds_name"	TEXT,
	"tds_join_table1"	TEXT,
	"tds_join_column1"	TEXT,
	"tds_join_table2"	TEXT,
	"tds_join_column2"	TEXT,
	"tds_join_type"	TEXT
);
INSERT INTO "DNS Join" ("tds_name","tds_join_table1","tds_join_column1","tds_join_table2","tds_join_column2","tds_join_type") VALUES ('t_f05_dns_m1728053448','pms.t_f05_dns_m1728053448','ne_sys_id','pms.t_dim_dns','ne_sys_id','inner'),
 ('t_f05_dns_m1728053448','pms.t_f05_dns_m1728053448','time_id','pms.t_dim_mdatetime','time_id','inner'),
 ('t_f15_dns_m1728053448','pms.t_f15_dns_m1728053448','ne_sys_id','pms.t_dim_dns','ne_sys_id','inner'),
 ('t_f15_dns_m1728053448','pms.t_f15_dns_m1728053448','time_id','pms.t_dim_mdatetime','time_id','inner'),
 ('t_f60_dns_m1728053448','pms.t_f60_dns_m1728053448','ne_sys_id','pms.t_dim_dns','ne_sys_id','inner'),
 ('t_f60_dns_m1728053448','pms.t_f60_dns_m1728053448','time_id','pms.t_dim_mdatetime','time_id','inner');
COMMIT;
