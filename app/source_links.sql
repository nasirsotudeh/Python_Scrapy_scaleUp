CREATE TABLE public.source_links (
    id int PRIMARY KEY,
    links varchar(255),
    rss varchar(255),
    status varchar(255)
);

CREATE TABLE public.RSS_data (
    id int PRIMARY KEY,
    RSS_Link varchar(255),
    rss varchar(255),
    status varchar(255)
);


