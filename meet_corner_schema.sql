-- Create a table to hold the type of meet: USAW, Mock, etc.
create table meet_type (
    id              integer primary key autoincrement not null,
    type            text
);

-- Main table to hold all meets
create table meets (
    id              integer primary key autoincrement not null,
    location        text not null,
    address         text,
    contact_email   text not null,
    event_link      text,
    start_date      date not null,
    end_date        date not null,
    meet_type       text not null references meet_type(type)
);