-- Show tables to verify creation
SELECT books
FROM information_schema.tables
WHERE table_schema = 'alx_book_store';