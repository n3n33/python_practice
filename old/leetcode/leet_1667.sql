SELECT user_id, concat(upper(substring(name,1,1)),
                       lower(substring(name,2,length(name)-1))) as name 
                       FROM Users
                       ORDER BY user_id
;