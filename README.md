# jdbc_to_jta
Change JDBC style SQL parameters to JTA style in a properties file.

Example, changes:
mySpecialFinder = from {0} as tc where t.id = ? and t.other_id=?

To:
mySpecialFinder = from {0} as tc where t.id = ?1 and t.other_id=?2

And changes:
select somecolumn from sometable t \
where t.id = ?

To:
select somecolumn from sometable t \
where t.id = ?1

Example usage:
jdbc_to_jta.py -i oldbranch/hibernate_query.properties -o newbranch/hibernate_query.properties
