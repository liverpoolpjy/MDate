# -*- coding: utf-8 -*-
import calendar
from datetime import datetime, timedelta

class MDate(object):
    def __init__(self):

        pass

    @staticmethod
    def last_second_in_last_month(cur):
        """
        获取上个月的最后一秒
        :param cur:
        :return:
        """
        min_time = cur.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        return min_time - timedelta(seconds=1)

    @staticmethod
    def next_month_date(d):
        """
        获取下个月的今天
        :param d:
        :return:
        """
        _year = d.year + (d.month // 12)
        _month = 1 if (d.month // 12) else d.month + 1
        next_month_len = calendar.monthrange(_year, _month)[1]
        next_month = d
        if d.day > next_month_len:
            next_month = next_month.replace(day=next_month_len)
        next_month = next_month.replace(year=_year, month=_month)
        return next_month

    @staticmethod
    def last_month_date(d):
        """
        获取上个月的今天
        :param d:
        :return:
        """
        _year = d.year - (1 if d.month == 1 else 0)
        _month = 12 if d.month == 1 else d.month - 1
        last_month_len = calendar.monthrange(_year, _month)[1]
        last_month = d
        if d.day > last_month_len:
            last_month = last_month.replace(day=last_month_len)
        last_month = last_month.replace(year=_year, month=_month)
        return last_month

    def month_list_for_recent_year(self, cursor):
        """
        近一年的月份列表
        :param cursor:
        :return:
        """
        _list = []
        for i in range(1, 13):
            _list.append(cursor.month)
            cursor = self.last_second_in_last_month(cursor)
        return _list[::-1]

    def start_and_end_time_list_for_recent_year(self, cursor):
        """
        近一年月份起止时间点列表
        :param cursor:
        :return:
        """
        _list = []
        for i in range(1, 13):
            start_time = cursor.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            end_time = cursor
            _list.append([start_time, end_time])
            cursor = self.last_second_in_last_month(cursor)
        return _list[::-1]

    def start_and_end_time_list_for_recent_month(self, cursor):
        """
        近一月起止时间点列表
        :param cursor:
        :return:
        """
        start_time = self.last_month_date(cursor)
        end_time = cursor
        return [start_time + timedelta(seconds=1), end_time]

    def start_and_end_time_list_for_recent_day(self, cursor):
        """
        近一天起止时间点列表
        :param cursor:
        :return:
        """
        start_time = cursor - timedelta(days=1)
        end_time = cursor
        return [start_time + timedelta(seconds=1), end_time]

    def start_and_end_time_list_for_recent_week(self, cursor):
        """
        近一周起止时间点列表
        :param cursor:
        :return:
        """
        start_time = cursor - timedelta(days=7)
        end_time = cursor
        return [start_time + timedelta(seconds=1), end_time]

    def recent_two_month_list(self, cursor):
        """
        最近两月起止时间列表
        :param cursor:
        :return:
        """
        this_month_list = self.start_and_end_time_list_for_recent_month(cursor)
        last_month = self.last_month_date(cursor)
        last_month_list = self.start_and_end_time_list_for_recent_month(last_month)
        return [last_month_list, this_month_list]

    def recent_two_week_list(self, cursor):
        """
        最近两周起止时间列表
        :param cursor:
        :return:
        """
        this_week_list = self.start_and_end_time_list_for_recent_week(cursor)
        last_week = cursor - timedelta(days=7)
        last_week_list = self.start_and_end_time_list_for_recent_week(last_week)
        return [last_week_list, this_week_list]

    def recent_two_day_list(self, cursor):
        """
        最近两天起止时间列表
        :param cursor:
        :return:
        """
        this_day_list = self.start_and_end_time_list_for_recent_day(cursor)
        last_day = cursor - timedelta(days=1)
        last_day_list = self.start_and_end_time_list_for_recent_day(last_day)
        return [last_day_list, this_day_list]