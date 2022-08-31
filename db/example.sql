/* テーブルriverを作成する */
CREATE TABLE river (
    id NUMERIC(4) PRIMARY KEY,
    name VARCHAR(32),
    length NUMERIC(8)
);

/* テーブルriverにレコードを挿入する */
INSERT INTO river(id, name, length) VALUES(1, '利根川', 322);
INSERT INTO river(id, name, length) VALUES(2, '信濃川', 367);
INSERT INTO river(id, name, length) VALUES(3, '相模川', 109);

/* テーブルriverのレコードを検索する */
SELECT * FROM river;

/* テーブルriverから、川の名前が'相模川'であるレコードを検索し、*/
/* 名称(name)と長さ(length)を表示する */
SELECT name, length FROM river WHERE name = ‘相模川’;

/* 200kmより長い川を検索し、長い順にソートする */
/* ASC: 昇順、DESC: 降順 */
SELECT * FROM river WHERE length > 200 ORDER BY length DESC;

/* テーブルriverを削除する */
DROP TABLE river;
