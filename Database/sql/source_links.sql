CREATE TABLE public.Web_links (
    link_id SERIAL PRIMARY KEY,
    links varchar(255),
    rss varchar(255),
    status varchar(255)
);

CREATE TABLE public.RSS_Fined (
    RSS_id INT GENERATED ALWAYS AS IDENTITY,
    link_id INT,
    rss varchar(255),
    status varchar(255),
        CONSTRAINT fk_links
            FOREIGN KEY(link_id)
	        REFERENCES Web_links(link_id)
);

CREATE TABLE public.RSS_data (
    id SERIAL PRIMARY KEY,
    News_Name varchar(255),
    RSS_Link varchar(255),
    RSS_Title varchar(255),
    RSS_Category varchar(255),
    source_id int
);


