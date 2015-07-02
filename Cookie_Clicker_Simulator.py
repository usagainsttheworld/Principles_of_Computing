"""
Cookie Clicker Simulator
"""

import simpleplot
import math

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
#SIM_TIME = 10000000000.0
SIM_TIME = 100.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """   
    def __init__(self):
        self._total_cookies = 0.0
        self._current_cookies = 0.0
        self._time = 0.0
        self._CPS = 1.0
        self._history = [(0.0, None, 0.0, 0.0)]
               
    def __str__(self):
        """
        Return human readable state
        """       
        message =	"\nTime:            "+ str(self._time) +"\n"\
                    "Current cookies: "+ str(self._current_cookies) +"\n"\
                    "CPS:             "+ str(self._CPS) +"\n"\
                    "Total cookies:   "+ str(self._total_cookies)

        return message
    
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._CPS
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return self._history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        wait_time = math.ceil((cookies - self._current_cookies)/self._CPS)
        return wait_time
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0:
            self._time += time
            self._current_cookies += self._CPS*time
            self._total_cookies += self._CPS*time
        else:
            return
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._current_cookies >= cost:
            self._current_cookies -= cost
            self._CPS += additional_cps
            self._history.append((self._time, item_name, cost, self._total_cookies))
        else:
            return

def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    clicker_info = build_info.clone()
    clicker_state = ClickerState()
    current_clicker = 0   
    cookies = clicker_state._current_cookies
    cps = clicker_state._CPS
    history = clicker_state._history
    time_left = duration - clicker_state._time
    
    while current_clicker <= duration:
        current_clicker += 1
        if clicker_state._time >duration:
            clicker_state.wait(time_left)
            return
        else:
            item_to_buy = strategy(cookies, cps, history, time_left, clicker_info)
            if item_to_buy == None:
                clicker_state.wait(time_left)
                return
            else:
                time_to_wait = clicker_state.time_until(clicker_info.get_cost(item_to_buy))
                if time_to_wait > duration:
                    clicker_state.wait(time_left)
                    return
                else:
                    clicker_state.wait(time_to_wait)
                    clicker_state.buy_item(item_to_buy, clicker_info.get_cost, clicker_info.get_cps)
                    clicker_info.update_item(item_to_buy)
    return clicker_state


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    return None

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    return None

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    return None
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
    
#run()
"""
game = ClickerState()
print game.get_cookies()
game.wait(12)
print game.get_cookies()
game.buy_item("farm", 15, 6)
print game.get_cookies()
print game.get_cps()
print game.get_history()
"""
test = provided.BuildInfo()
simulate_clicker(test, SIM_TIME, strategy_cursor_broken)
    




