#! /usr/bin/env python
from modules import top_three_articles, top_three_authors, error_logs


def main():
    top_three_articles.print_top_three_articles()
    top_three_authors.print_top_three_authors()
    error_logs.print_error_logs()


if __name__ == '__main__':
    main()
