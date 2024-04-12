from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Transaction
from . import db
import json
from datetime import datetime
from itertools import chain
from collections import defaultdict

views = Blueprint('views', __name__)

months_mapping = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

categories_mapping = {
    "1": "Housing",
    "2": "Transportation",
    "3": "Food",
    "4": "Healthcare",
    "5": "Insurance",
    "6": "Debt payments",
    "7": "Entertainment",
    "8": "Personal care",
    "9": "Education",
    "10": "Investments",
    "11": "Other",
    "12": "Income"
}


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        month = request.json.get('month')
        transactions = Transaction.query.filter_by(user_id=current_user.id, month=month).all()
        total_earned = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'income')
        total_spent = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'expense')
        
        # Calculate expenses by category
        category_data = defaultdict(float)
        for transaction in transactions:
            if transaction.transaction_type == 'expense':
                category_data[transaction.category] += transaction.amount

        # Convert defaultdict to regular dict
        category_data = dict(category_data)

        print("Category Data:", category_data)

        return jsonify({
            'totalEarned': total_earned, 
            'totalSpent': total_spent,
            'categoryData': category_data
        })
    return render_template("home.html", user=current_user)



@views.route('/expenses', methods=['GET', 'POST'])
@login_required
def expenses():
    if request.method == "POST":
        month = request.form.get("month")
        if not month:
            flash('Month is required.', category='error')
            return render_template("expenses.html", user=current_user)
        amount_str = request.form.get("expenses")
        if not amount_str:
            flash('Amount is required.', category='error')
            return render_template("expenses.html", user=current_user)
        try:
            amount = float(amount_str)
        except ValueError:
            flash('Invalid amount. Please enter a valid number.', category='error')
            return render_template("expenses.html", user=current_user)
        
        # Validate category
        category = request.form.get("category")
        if not category:
            flash('Category is required.', category='error')
            return render_template("expenses.html", user=current_user)
        
        transaction_type = 'expense'
        
        # Create a new Expense object with the retrieved data
        new_expense = Transaction(timestamp=datetime.utcnow(), 
                                  transaction_type=transaction_type, month=month, 
                                  amount=amount, category=category, user_id=current_user.id)
        
        # Add the new expense to the database session
        db.session.add(new_expense)
        db.session.commit()
        # Redirect the user to the home page
        return redirect(url_for('views.home'))
        
    return render_template("expenses.html", user=current_user)


@views.route('/income', methods=['GET', 'POST'])
@login_required
def income():
    if request.method == "POST":
        month = request.form.get("month")
        if not month:
            flash('Month is required.', category='error')
            return render_template("income.html", user=current_user)
        amount_str = request.form.get("income")
        if not amount_str:
            flash('Amount is required.', category='error')
            return render_template("income.html", user=current_user)
        try:
            amount = float(amount_str)
        except ValueError:
            flash('Invalid amount. Please enter a valid number.', category='error')
            return render_template("income.html", user=current_user)
        
        transaction_type = 'income'
        category = "12"
        
        # Create a new Expense object with the retrieved data
        new_income = Transaction(timestamp=datetime.utcnow(), 
                                 transaction_type=transaction_type, month=month, 
                                 amount=amount, category=category, user_id=current_user.id)
        
        # Add the new expense to the database session
        db.session.add(new_income)
        db.session.commit()
        # Redirect the user to the home page
        return redirect(url_for('views.home'))
        
    return render_template("income.html", user=current_user)


@views.route('/history', methods=['GET', 'POST'])
@login_required
def history():
    user_transactions = Transaction.query.filter_by(user_id=current_user.id)\
                                         .order_by(Transaction.timestamp.desc())\
                                         .all()
    
    return render_template("history.html", user=current_user, 
                           user_transactions=user_transactions,
                           months_mapping=months_mapping,
                           categories_mapping=categories_mapping)

@views.route('/delete_transaction/<int:transaction_id>', methods=['POST'])
@login_required
def delete_transaction(transaction_id):
    print("transaction_id")
    # Retrieve the transaction by ID
    transaction = Transaction.query.get(transaction_id)
    
    if transaction:
        # Delete the transaction
        db.session.delete(transaction)
        db.session.commit()
        flash('Transaction deleted successfully!', category='success')
    else:
        flash('Transaction not found!', category='error')
    
    return redirect(url_for('views.history'))

